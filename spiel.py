import tkinter
import zielObjekt
import random

class spiel:

    def erzeugeZiele(self, anzahl, minY, maxY):
        erzeugteZiele = []

        for i in range(anzahl):
            ziel = zielObjekt.zielObjekt()
            ziel.x = 300
            ziel.y = random.randint(minY, maxY)
            erzeugteZiele.append(ziel)
        return erzeugteZiele

    def start(self):
        self.hauptschleife()
        self.spiel_fenster.mainloop()

    def hauptschleife(self):
        self.aktualisiere()
        self.zeichne()

        self.spiel_fenster.after(10, self.hauptschleife)

    def zeichne(self):
        for ziel in self.ziele:
            ziel.zeichne(self.spielfeld)

    def aktualisiere(self):
        for ziel in self.ziele:
            ziel.bewegeDich(1)
            if(not ziel.valide):
                self.spielfeld.delete(ziel.zeichnung)
                self.ziele.remove(ziel)

    def __init__(self):
        #Lege das FPS(Frames per second)-limit fest
        self.gewuenschteFPS = 60

        #Erstelle das Programmfenster und lege seine Größe fest.
        self.spiel_fenster = tkinter.Tk()
        self.spiel_fenster.resizable(width=False, height=False)
        self.spiel_fenster.geometry("600x400")

        #Erstelle das Spielfeld und lege seine Größe fest.
        self.spielfeld = tkinter.Canvas(width=600,height=300)

        #Zeichne den Spielfeldhintergrund
        self.spielfeld.create_rectangle(0, 0, 600, 300,
                                         fill="#000",outline="")
        self.spielfeld.pack()

        #Starte das Spiel
        self.ziele = self.erzeugeZiele(3, 0, 300)

        self.start()

if(__name__=="__main__"):
    spiel()