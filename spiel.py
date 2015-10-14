import tkinter
import zielObjekt
import random
import spieler
import time

class Konst:
    """Beinhaltet wichtige Konstanten"""

    FENSTER_HOEHE = 400
    FENSTER_BREITE = 600

    SPIELFELD_HOEHE = 300
    SPIELFELD_BREITE = 600
    SPIELFELD_FARBE = "#000000"

    #FPS (frames per second) - Aufrufe der Hauptschleife pro Sekunde
    FPS=40

class spiel:
    def erzeugeZiele(self, anzahl, minY, maxY):
        erzeugteZiele = []

        for i in range(anzahl):
            ziel = zielObjekt.erzeugeZiel(600, 600, minY, maxY,
                                          self.spielfeld)
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

        self.spielfigur.zeichne(self.spielfeld)

    def aktualisiere(self):
        self.spielfigur.y = self.maushoehe

        if(time.time() - self.letzteWelle > self.wellenabstand):
            self.erzeugeZiele(random.randint(1, 3), 50, 250)
            self.letzteWelle = time.time()

        for ziel in self.ziele:
            ziel.bewegeDich(4)
           
            if(ziel.x <= self.spielfigur.x + self.spielfigur.hoehe):
                if((ziel.y + ziel.groesse >= self.spielfigur.y) and 
                        (ziel.y <= self.spielfigur.y + self.spielfigur.hoehe)):
                    ziel.valide = False

            if(not ziel.valide):
                self.spielfeld.delete(ziel.zeichnung)
                self.ziele.remove(ziel)


    def mausBewegt(self, ereignis):
        self.maushoehe = ereignis.y

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
        self.spielfigur = spieler.spieler(breite=30, hoehe=20)
        self.maushoehe = self.spielfigur.y

        #Lege Eventhandeling die Mausbewegung fest
        self.spielfeld.bind('<Motion>', self.mausBewegt)

        #Lege den Abstand zwischen den Wellen fest
        self.wellenabstand = 0.9

        #Starte das Spiel
        self.ziele = []

        self.start()

if(__name__=="__main__"):
    spiel()