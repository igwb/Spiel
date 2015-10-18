import tkinter
import zielObjekt
import random
import spieler
import spielfeld
import time
import statistik


#FPS (frames per second) - Aufrufe der Hauptschleife pro Sekunde
FPS=40

FENSTER_HOEHE = 310
FENSTER_BREITE = 600


SPIELER_TREIBSTOFFVERBRAUCH = 1.5 / FPS

WELLEN_ABSTAND = 0.9
WELLEN_GROESSE_MIN = 1
WELLEN_GROESSE_MAX = 3
WELLEN_START_X = 600
WELLEN_START_MIN_Y = 20
WELLEN_START_MAX_Y = spielfeld.HOEHE - 20
WELLEN_GESCHWINDIGKEIT = 3

#Gewichtung der Zielobjekt-Typen 
ZIELOBJEKT_WAHRSCHEINLICHKEITEN = [5, 2]

class Spiel:
    def __init__(self):
        #Erstelle das Programmfenster und lege seine Größe fest.
        self.spielfenster = tkinter.Tk()
        self.spielfenster.resizable(width=False, height=False)
        self.spielfenster.geometry(str(FENSTER_BREITE) + "x" + 
                                   str(FENSTER_HOEHE))
        #Erstelle das Spielfeld
        self.spielfeld = spielfeld.Spielfeld()
        #Erstelle die Statistikanzeige
        self.statistik = statistik.Statistik()
        #Initalisiere die Spielfigur
        self.spielfigur = spieler.spieler(self.spielfeld.maluntergrund)
        #Lege Eventhandeling fest
        self.spielfeld.maluntergrund.bind('<Motion>', self.mausBewegt)
        self.spielfeld.maluntergrund.bind("<Button-1>", self.mausGeklickt)
        self.spielfeld.maluntergrund.bind_all('<Key>', self.tasteGedrueckt)
        #Starte das Spiel
        self.ziele = []
        self.zeichnung_pause = None
        self.start()

    def start(self):
        self.spiel_laeuft = True

        self.letzteWelle = time.time()
        self.startzeitpunkt = time.time()
        self.letzte_hauptschleife = time.time()

        self.hauptschleife()
        self.spielfenster.mainloop()

    def neuStart(self):
        self.setzeSpielLaeuft(False)

        self.letzteWelle = time.time()
        self.startzeitpunkt = time.time()
        self.letzte_hauptschleife = time.time()

        self.spielfeld.maluntergrund.delete("ALL")
        self.ziele = []
        self.statistik.reset()
        self.spielfigur.reset()
        self.zeichne()

    def hauptschleife(self):
        if(not self.spiel_laeuft):
            self.spielfenster.after(10, self.hauptschleife)
            return

        self.aktualisiere()
        self.zeichne()

        jetzt = time.time()
        verstrichene_zeit = jetzt - self.letzte_hauptschleife
        self.letzte_hauptschleife = jetzt

        optimale_verstrichene_zeit = 1./FPS

        schlafenszeit = int((optimale_verstrichene_zeit - verstrichene_zeit) 
                            * 1000)

        if(schlafenszeit > 0):
            self.spielfenster.after(schlafenszeit, self.hauptschleife)
        else:
            print(str(schlafenszeit * -1) + "ms zu langsam!")
            self.spielfenster.after(10, self.hauptschleife)

    def aktualisiere(self):
        if(self.statistik.treibstoff <= 0):
            self.neuStart()
            return

        self.statistik.verbraucheTreibstoff(SPIELER_TREIBSTOFFVERBRAUCH)
        self.statistik.erhoehePunktzahl(0.1)

        #Generiere eine neue Welle von Zielen
        if(time.time() - self.letzteWelle > WELLEN_ABSTAND):
            wellen_groesse = random.randint(WELLEN_GROESSE_MIN,
                                            WELLEN_GROESSE_MAX)
            self.erzeugeZiele(wellen_groesse)
            self.letzteWelle = time.time()

        #Bewege die Ziele
        for ziel in self.ziele:
            ziel.bewegeDich(WELLEN_GESCHWINDIGKEIT)
           
            if(self.istKollidierend(ziel.x, ziel.y, ziel.hoehe, ziel.breite,
                               self.spielfigur.x, self.spielfigur.y,
                               self.spielfigur.hoehe, self.spielfigur.breite)):
                    self.statistik.zielGesammelt(ziel)
                    ziel.valide = False

            if(not ziel.valide):
                self.spielfeld.maluntergrund.delete(ziel.zeichnung)
                self.ziele.remove(ziel)

    def istKollidierend(self, x1, y1, hoehe1, breite1, x2, y2, hoehe2, breite2):
        if (y1 + hoehe1 < y2):
            return False
        if(y1 > y2 + hoehe2):
            return False
        if (x1 + breite1 < x2):
            return False
        if(x1 > x2 + breite2):
            return False 
        return True

    def zeichne(self):
        self.spielfeld.zeichneHintergrund()

        #Zeichne alle Ziele
        for ziel in self.ziele:
            ziel.aktualisiere()
        #Zeichne die Spielfigur
        self.spielfigur.aktualisiere()
        #Zeichne die Punktzahl und den vorhandenen Treibstoff
        self.statistik.aktualisiere()

    def erzeugeZiele(self, anzahl):
        erzeugteZiele = []

        for i in range(anzahl):
            y = random.randint(WELLEN_START_MIN_Y, WELLEN_START_MAX_Y)

            liste = []
            for t in range(len(ZIELOBJEKT_WAHRSCHEINLICHKEITEN)):
                liste += [str(t)] * ZIELOBJEKT_WAHRSCHEINLICHKEITEN[t]
            typ = int(random.choice(liste))

            ziel = zielObjekt.zielObjekt(self.spielfeld.maluntergrund,
                                         WELLEN_START_X, y, typ)

            erzeugteZiele.append(ziel)
        
        self.ziele += erzeugteZiele
    
    def setzeSpielLaeuft(self, zustand):
        self.spiel_laeuft = zustand

        if(self.spiel_laeuft):
            self.spielfeld.maluntergrund.delete(self.zeichnung_pause)
            self.zeichnung_pause = None
        else:
            if(self.zeichnung_pause != None):
                return
            self.zeichnung_pause = self.spielfeld.maluntergrund.create_text(
                                                    FENSTER_BREITE / 2,
                                                    spielfeld.HOEHE / 2,
                                                    text="PAUSE",
                                                    font=("Arial", 28),
                                                    fill="#ffffff")

    def tasteGedrueckt(self, ereignis):
        if(ereignis.char.lower() == "p"):
            self.setzeSpielLaeuft(False)
        if(ereignis.char.lower() == "r"):
            self.neuStart()

    def mausBewegt(self, ereignis):
        self.spielfigur.setzePosition(ereignis.x, ereignis.y)

    def mausGeklickt(self, ereignis):
        if(self.istKollidierend(ereignis.x, ereignis.y, 1, 1,
                           self.spielfigur.x, self.spielfigur.y,
                           self.spielfigur.hoehe, self.spielfigur.breite)):
            self.setzeSpielLaeuft(not self.spiel_laeuft)

if(__name__=="__main__"):
    Spiel()