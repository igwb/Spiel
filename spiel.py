import tkinter
import zielObjekt
import random
import spieler

class spiel:

    def erzeugeZiele(self, anzahl, minY, maxY):
        erzeugteZiele = []

        for i in range(anzahl):
            ziel = zielObjekt.erzeugeZiel(600,600,minY,maxY)
            erzeugteZiele.append(ziel)
        
        self.ziele += erzeugteZiele

    def start(self):
        self.hauptschleife()
        self.spielfenster.mainloop()

    def hauptschleife(self):
        self.aktualisiere()
        self.zeichne()

        self.spielfenster.after(10, self.hauptschleife)

    def zeichne(self):
        for ziel in self.ziele:
            ziel.zeichne(self.spielfeld)

        self.spielfigur.zeichne(self.spielfeld)

    def aktualisiere(self):

        self.spielfigur.y = self.maushoehe

        if(random.randint(0,100) > 95):
            self.erzeugeZiele(random.randint(1,4),0,300)

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
        #print(str(ereignis.x) + " - " + str(ereignis.y))
        self.maushoehe = ereignis.y

    def __init__(self):
        #Lege das FPS(Frames per second)-limit fest
        self.gewuenschteFPS = 60

        #Erstelle das Programmfenster und lege seine Größe fest.
        self.spielfenster = tkinter.Tk()
        self.spielfenster.resizable(width=False, height=False)
        self.spielfenster.geometry("600x400")

        #Erstelle das Spielfeld und lege seine Größe fest.
        self.spielfeld = tkinter.Canvas(width=600,height=300)

        #Zeichne den Spielfeldhintergrund
        self.spielfeld.create_rectangle(0, 0, 600, 300,
                                         fill="#000",outline="")
        
        self.spielfeld.pack()

        #Initalisiere die Spielfigur
        self.spielfigur = spieler.spieler(breite=30, hoehe=20)
        self.maushoehe = self.spielfigur.y

        #Lege Eventhandeling für Tasten fest
        self.spielfeld.bind('<Motion>', self.mausBewegt)

        #Starte das Spiel
        self.ziele = []

        self.start()

if(__name__=="__main__"):
    spiel()