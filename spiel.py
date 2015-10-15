import tkinter
import zielObjekt
import random
import spieler
import time

class Konst:
    """Beinhaltet wichtige Konstanten"""

    FENSTER_HOEHE = 400
    FENSTER_BREITE = 600

    SPIELFELD_HOEHE = 250
    SPIELFELD_BREITE = 600
    SPIELFELD_FARBE = "#000000"

    SPIELER_GRAFIK = "spieler.png"
    SPIELER_START_X = 60
    SPIELER_START_Y = SPIELFELD_HOEHE / 2

    WELLEN_ABSTAND = 0.5
    WELLEN_GROESSE_MIN = 1
    WELLEN_GROESSE_MAX = 3

    #Gewichtung der Zielobjekt-Typen 
    ZIELOBJEKT_WAHRSCHEINLICHKEITEN = [4, 1]

    #FPS (frames per second) - Aufrufe der Hauptschleife pro Sekunde
    FPS=40

class spiel:
    def erzeugeZiele(self, anzahl, minY, maxY):
        erzeugteZiele = []

        for i in range(anzahl):
            y = random.randint(minY, maxY)

            liste = []
            for t in range(len(Konst.ZIELOBJEKT_WAHRSCHEINLICHKEITEN)):
                liste += [str(t)] * Konst.ZIELOBJEKT_WAHRSCHEINLICHKEITEN[t]
            typ = int(random.choice(liste))

            ziel = zielObjekt.zielObjekt(600, y, typ, self.spielfeld)

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
        for ziel in self.ziele:
            ziel.aktualisiere()

        self.spielfigur.aktualisiere(self.spielfeld)

    def aktualisiere(self):
        if(time.time() - self.letzteWelle > Konst.WELLEN_ABSTAND):
            groesse = random.randint(Konst.WELLEN_GROESSE_MIN, Konst.WELLEN_GROESSE_MAX)
            self.erzeugeZiele(groesse, 50, 250)
            self.letzteWelle = time.time()

        for ziel in self.ziele:
            ziel.bewegeDich(4)
           
            if((ziel.x <= self.spielfigur.x + self.spielfigur.breite) and 
               (ziel.x >= self.spielfigur.x)):
                if((ziel.y + ziel.hoehe >= self.spielfigur.y) and 
                   (ziel.y <= self.spielfigur.y + self.spielfigur.hoehe)):
                    ziel.valide = False

            if(not ziel.valide):
                self.spielfeld.delete(ziel.zeichnung)
                self.ziele.remove(ziel)


    def mausBewegt(self, ereignis):
        self.spielfigur.setzePosition(self.spielfigur.zielX, ereignis.y)

    def __init__(self):
        #Erstelle das Programmfenster und lege seine Größe fest.
        self.spielfenster = tkinter.Tk()
        self.spielfenster.resizable(width=False, height=False)
        self.spielfenster.geometry(str(Konst.FENSTER_BREITE) + "x" + 
                                   str(Konst.FENSTER_HOEHE))

        #Erstelle das Spielfeld und lege seine Größe fest.
        self.spielfeld = tkinter.Canvas(width=Konst.SPIELFELD_BREITE,
                                        height=Konst.SPIELFELD_HOEHE)

        #Zeichne den Spielfeldhintergrund
        self.spielfeld.create_rectangle(0, 0, Konst.SPIELFELD_BREITE,
                                        Konst.SPIELFELD_HOEHE,
                                        fill=Konst.SPIELFELD_FARBE,
                                        outline="")
        self.spielfeld.pack()

        #Initalisiere die Spielfigur
        bild = tkinter.PhotoImage(file=Konst.SPIELER_GRAFIK)
        self.spielfigur = spieler.spieler(Konst.SPIELER_START_X, 
                                          Konst.SPIELER_START_Y, bild)

        #Lege Eventhandeling die Mausbewegung fest
        self.spielfeld.bind('<Motion>', self.mausBewegt)

        #Starte das Spiel
        self.ziele = []
        self.start()

if(__name__=="__main__"):
    spiel()