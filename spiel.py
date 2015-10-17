import tkinter
import zielObjekt
import random
import spieler
import spielfeld
import time
import statistik

class Konst:
    """Beinhaltet wichtige Konstanten"""

    #FPS (frames per second) - Aufrufe der Hauptschleife pro Sekunde
    FPS=40

    FENSTER_HOEHE = 310
    FENSTER_BREITE = 600

    SPIELER_START_X = 60
    SPIELER_START_Y = spielfeld.Konst.SPIELFELD_HOEHE / 2
    SPIELER_TREIBSTOFFVERBRAUCH = 1.5 / FPS

    WELLEN_ABSTAND = 0.9
    WELLEN_GROESSE_MIN = 1
    WELLEN_GROESSE_MAX = 3
    WELLEN_START_X = 600
    WELLEN_START_MIN_Y = 20
    WELLEN_START_MAX_Y = spielfeld.Konst.SPIELFELD_HOEHE - 20
    WELLEN_GESCHWINDIGKEIT = 3

    #Gewichtung der Zielobjekt-Typen 
    ZIELOBJEKT_WAHRSCHEINLICHKEITEN = [5, 2]

class spiel:
    def erzeugeZiele(self, anzahl):
        erzeugteZiele = []

        for i in range(anzahl):
            y = random.randint(Konst.WELLEN_START_MIN_Y,
                               Konst.WELLEN_START_MAX_Y)

            liste = []
            for t in range(len(Konst.ZIELOBJEKT_WAHRSCHEINLICHKEITEN)):
                liste += [str(t)] * Konst.ZIELOBJEKT_WAHRSCHEINLICHKEITEN[t]
            typ = int(random.choice(liste))

            ziel = zielObjekt.zielObjekt(Konst.WELLEN_START_X, y,
                                         typ, self.spielfeld.maluntergrund)

            erzeugteZiele.append(ziel)
        
        self.ziele += erzeugteZiele

    def start(self):
        self.letzteWelle = time.time()
        self.startzeitpunkt = time.time()
        self.letzte_hauptschleife = time.time()

        self.hauptschleife()
        self.spielfenster.mainloop()

    def hauptschleife(self):
        self.aktualisiere()
        self.zeichne()

        jetzt = time.time()
        verstrichene_zeit = jetzt - self.letzte_hauptschleife
        self.letzte_hauptschleife = jetzt

        optimale_verstrichene_zeit = 1./Konst.FPS

        schlafenszeit = int((optimale_verstrichene_zeit - verstrichene_zeit) 
                            * 1000)

        if(schlafenszeit > 0):
            self.spielfenster.after(schlafenszeit, self.hauptschleife)
        else:
            print(str(schlafenszeit * -1) + "ms zu langsam!")
            self.spielfenster.after(10, self.hauptschleife)

    def zeichne(self):

        self.spielfeld.zeichneHintergrund()

        #Zeichne alle Ziele
        for ziel in self.ziele:
            ziel.aktualisiere()

        #Zeichne die Spielfigur
        self.spielfigur.aktualisiere(self.spielfeld.maluntergrund)

        #Zeichne die Punktzahl und den vorhandenen Treibstoff
        self.statistik.aktualisiere()

    def aktualisiere(self):

        self.statistik.verbraucheTreibstoff(Konst.SPIELER_TREIBSTOFFVERBRAUCH)
        self.statistik.erhoehePunktzahl(0.1)

        #Generiere eine neue Welle von Zielen
        if(time.time() - self.letzteWelle > Konst.WELLEN_ABSTAND):
            wellen_groesse = random.randint(Konst.WELLEN_GROESSE_MIN,
                                            Konst.WELLEN_GROESSE_MAX)
            self.erzeugeZiele(wellen_groesse)
            self.letzteWelle = time.time()

        #Bewege die Ziele
        for ziel in self.ziele:
            ziel.bewegeDich(Konst.WELLEN_GESCHWINDIGKEIT)
           
            if((ziel.x <= self.spielfigur.x + self.spielfigur.breite) and 
               (ziel.x >= self.spielfigur.x)):
                if((ziel.y + ziel.hoehe >= self.spielfigur.y) and 
                   (ziel.y <= self.spielfigur.y + self.spielfigur.hoehe)):
                    self.statistik.zielGesammelt(ziel)
                    ziel.valide = False

            if(not ziel.valide):
                self.spielfeld.maluntergrund.delete(ziel.zeichnung)
                self.ziele.remove(ziel)

    def mausBewegt(self, ereignis):
        self.spielfigur.setzePosition(ereignis.x, ereignis.y)

    def __init__(self):
        #Erstelle das Programmfenster und lege seine Größe fest.
        self.spielfenster = tkinter.Tk()
        self.spielfenster.resizable(width=False, height=False)
        self.spielfenster.geometry(str(Konst.FENSTER_BREITE) + "x" + 
                                   str(Konst.FENSTER_HOEHE))
        #Erstelle das Spielfeld
        self.spielfeld = spielfeld.Spielfeld()
        #Erstelle die Statistikanzeige
        self.statistik = statistik.Statistik()
        #Initalisiere die Spielfigur
        self.spielfigur = spieler.spieler(Konst.SPIELER_START_X, 
                                          Konst.SPIELER_START_Y)
        #Lege Eventhandeling für die Mausbewegung fest
        self.spielfeld.maluntergrund.bind('<Motion>', self.mausBewegt)

        #Starte das Spiel
        self.ziele = []
        self.start()

if(__name__=="__main__"):
    spiel()