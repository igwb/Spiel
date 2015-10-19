import tkinter
import random
import time
import zielObjekt
import spieler
import spielfeld
import statistik

# FPS (frames per second) - Aufrufe der Hauptschleife pro Sekunde
FPS = 40

FENSTER_HOEHE = 310
FENSTER_BREITE = 600

PUNKTE_PRO_FRAME = 1 / FPS
SPIELER_TREIBSTOFFVERBRAUCH = 1.8 / FPS

WELLEN_ABSTAND = 0.9
WELLEN_GROESSE_MIN = 1
WELLEN_GROESSE_MAX = 3
WELLEN_START_X = FENSTER_BREITE + 30
WELLEN_START_MIN_Y = 20
WELLEN_START_MAX_Y = spielfeld.HOEHE - 20

# Gewichtung der Zielobjekt-Typen 
ZIELOBJEKT_WAHRSCHEINLICHKEITEN = [5, 2]

class Spiel:
    def __init__(self):
        """Instanziiere. Erstellt das Hauptspielfenster und initialisiert
        die einzelnen Spielkomponenten.
        """
        # Erstelle das Hauptspielfenster und lege seine Größe fest.
        self.fenster = tkinter.Tk()
        self.fenster.resizable(width=False, height=False)
        self.fenster.geometry(str(FENSTER_BREITE) + "x" + 
                                   str(FENSTER_HOEHE))
        # Erstelle das Spielfeld
        self.spielfeld = spielfeld.Spielfeld()
        # Erstelle die Statistikanzeige
        self.statistik = statistik.Statistik()
        # Initalisiere die Spielfigur
        self.spielfigur = spieler.Spieler(self.spielfeld.leinwand)
        # Lege Eventhandeling fest
        self.spielfeld.leinwand.bind('<Motion>', self.mausBewegt)
        self.spielfeld.leinwand.bind("<Button-1>", self.mausGeklickt)
        self.spielfeld.leinwand.bind_all('<Key>', self.tasteGedrueckt)
        # Initialisiere Variablen
        self.ziele = []
        self.zeichnung_pause = None
        # Starte das Spiel
        self.start()

    def start(self):
        """Startet das Spiel."""
        self.spiel_laeuft = True

        self.letzteWelle = time.time()
        self.startzeitpunkt = time.time()
        self.letzte_hauptschleife = time.time()

        self.hauptschleife()
        self.fenster.mainloop()

    def neustart(self):
        """Startet das Spiel neu."""
        # Pausiere das Spiel
        self.setzeSpielLaeuft(False)
        # Setze die Start- und Wellenzeiten zurueck.
        self.letzteWelle = time.time()
        self.startzeitpunkt = time.time()
        self.letzte_hauptschleife = time.time()
        # Loesche alle ZielObjekte
        self.spielfeld.leinwand.delete("ALL")
        self.ziele = []
        # Setze die Statistik und den Spieler zurueck.
        self.statistik.reset()
        self.spielfigur.reset()
        # Zeichne das Spielfeld neu.
        self.zeichne()

    def hauptschleife(self):
        """Fuehrt das Spiel aus. Wird regelmaessig aufgerufen."""
        # Breche ab, falls das Spiel pausiert ist.
        if(not self.spiel_laeuft):
            self.fenster.after(10, self.hauptschleife)
            return
        # Fuehre das Spiel aus.
        self.aktualisiere()
        self.zeichne()
        # Berechne die vergangene Zeit seit dem letzten Aufruf der Hauptschleife
        jetzt = time.time()
        verstrichene_zeit = jetzt - self.letzte_hauptschleife
        self.letzte_hauptschleife = jetzt
        # Berechne die optimale Zeit, die von Hauptschleife zu Hauptschleife
        # vergehen sollte.
        optimale_verstrichene_zeit = 1./FPS
        # Berechne die Differenz zwischen der optimalen und der tatsaechlich
        # vergangenen Zeit und halte das Spiel solange an.
        schlafenszeit = int((optimale_verstrichene_zeit - verstrichene_zeit) 
                            * 1000)
        if(schlafenszeit > 0):
            self.fenster.after(schlafenszeit, self.hauptschleife)
        else:
            print(str(schlafenszeit * -1) + "ms zu langsam!")
            self.fenster.after(10, self.hauptschleife)

    def aktualisiere(self):
        """Aktualisiert den Spielzustand."""
        # Starte das Spiel neu, falls der Treibstoff alle ist.
        if(self.statistik.treibstoff <= 0):
            self.neustart()
            return
        # Verbrauche Treibstoff und erhoehe die Punktzahl.
        self.statistik.verbraucheTreibstoff(SPIELER_TREIBSTOFFVERBRAUCH)
        self.statistik.erhoehePunktzahl(PUNKTE_PRO_FRAME)
        # Generiere eine neue Welle von Zielen.
        if(time.time() - self.letzteWelle > WELLEN_ABSTAND):
            self.erzeugeWelle()
        # Bewege die Ziele.
        for ziel in self.ziele:
            ziel.bewegeDich()
            if(self.istKollidierend(ziel.abgrenzung(),
                                    self.spielfigur.abgrenzung())):
                    self.statistik.zielGesammelt(ziel)
                    ziel.valide = False

    def zeichne(self):
        """Zeichnet das Spiel."""
        #Zeichne den Spielfeldhintergrund.
        self.spielfeld.zeichneHintergrund()
        # Zeichne die Ziele.
        for ziel in self.ziele:
            if(ziel.valide):
                ziel.aktualisiere()
            else:
                self.spielfeld.leinwand.delete(ziel.zeichnung)
                self.ziele.remove(ziel)
        # Zeichne die Spielfigur
        self.spielfigur.aktualisiere()
        # Zeichne die Punktzahl und den vorhandenen Treibstoff
        self.statistik.aktualisiere()

    def erzeugeWelle(self):
        erzeugteZiele = []
        #Lege die Groesse der Welle fest.
        anzahl = random.randint(WELLEN_GROESSE_MIN, WELLEN_GROESSE_MAX)
        for i in range(anzahl):
            y = random.randint(WELLEN_START_MIN_Y, WELLEN_START_MAX_Y)
            # Waehle den Typ des Zielobjekts unter beruecksichtigung der
            # Gewichtung aus.
            liste = []
            for t in range(len(ZIELOBJEKT_WAHRSCHEINLICHKEITEN)):
                liste += [str(t)] * ZIELOBJEKT_WAHRSCHEINLICHKEITEN[t]
            typ = int(random.choice(liste))
            # Erzeuge das Ziel.
            ziel = zielObjekt.ZielObjekt(self.spielfeld.leinwand,
                                         WELLEN_START_X, y, typ)
            erzeugteZiele.append(ziel)
        # Fuege die erzeugten Ziele zur Liste der Ziele hinzu.
        self.ziele += erzeugteZiele
        # Speichere die Erzeugungszeit der Welle.
        self.letzteWelle = time.time()
    
    def setzeSpielLaeuft(self, zustand):
        """Haellt das Spiel an oder setzt es fort."""
        self.spiel_laeuft = zustand
        if(self.spiel_laeuft):
            # Loesche den Pause-Bildschirm
            self.spielfeld.leinwand.delete(self.zeichnung_pause)
            self.zeichnung_pause = None
        else:
            # Zeichne den Pause-Bildschirm
            if(self.zeichnung_pause != None):
                return
            self.zeichnung_pause = self.spielfeld.leinwand.create_text(
                                                    FENSTER_BREITE / 2,
                                                    spielfeld.HOEHE / 2,
                                                    text="PAUSE",
                                                    font=("Arial", 28),
                                                    fill="#ffffff")

    def istKollidierend(self, abgrenzung1, abgrenzung2):
        """Ueberprueft ob zwei Objekte miteinander Kollidieren."""
        if (abgrenzung1['y'] + abgrenzung1['hoehe']  < abgrenzung2['y']):
            return False
        if(abgrenzung1['y'] > abgrenzung2['y'] + abgrenzung2['hoehe']):
            return False
        if (abgrenzung1['x'] + abgrenzung1['breite'] < abgrenzung2['x']):
            return False
        if(abgrenzung1['x'] > abgrenzung2['x'] + abgrenzung2['breite']):
            return False 
        return True

    def tasteGedrueckt(self, ereignis):
        if(ereignis.char.lower() == "p"):
            self.setzeSpielLaeuft(False)
        if(ereignis.char.lower() == "r"):
            self.neustart()

    def mausBewegt(self, ereignis):
        """Wird aufgerufen, wenn sich die Maus bewegt und setzt den Spieler
        an die Position des Mauszeigers.
        """
        self.spielfigur.setzePosition(ereignis.x, ereignis.y)

    def mausGeklickt(self, ereignis):
        """Wird aufgerufen, wenn die linke Maustaste betaetigt wird und 
        pausiert das Spiel bzw. setzt es fort, wenn auf den Spieler gecklickt
        wurde.
        """
        abgrenzung = dict([('x', ereignis.x), ('y', ereignis.y),
                           ('hoehe', 0), ('breite', 0)])
        if(self.istKollidierend(abgrenzung, self.spielfigur.abgrenzung())):
            self.setzeSpielLaeuft(not self.spiel_laeuft)

if(__name__== "__main__"):
    Spiel()