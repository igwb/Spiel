import tkinter
import gegenstand
import zeichenManager

class spiel:

    def erzeugeGegenstaende(self, anzahl):
        erzeugteObjekte = []

        for i in range(anzahl):
            erzeugteObjekte.append(gegenstand.gegenstand())
        return erzeugteObjekte

    def hauptschleife(self):
        self.aktualisiere()
        self.zeichne()

        self.spiel_fenster.after(10, self.hauptschleife)

    def zeichne(self):
        print("zeichnet")
        zeichenManager.zeichne(self.spiel_feld)

    def aktualisiere(self):
        for ziel in self.ziele:
            ziel.bewegeDich(1)

    def __init__(self):
        #Lege das FPS(Frames per second)-limit fest
        self.gewuenschteFPS = 60

        #Erstelle das Programmfenster und lege seine Größe fest.
        self.spiel_fenster = tkinter.Tk()
        self.spiel_fenster.resizable(width=False, height=False)
        self.spiel_fenster.geometry("600x400")

        #Erstelle das Spielfeld und lege seine Größe fest.
        self.spiel_feld = tkinter.Canvas(width=600,height=300)

        #Zeichne den Spielfeldhintergrund
        self.spiel_feld.create_rectangle(0, 0, 600, 300,
                                         fill="#000",outline="")
        self.spiel_feld.pack()

        #Starte das Spiel
        self.ziele = self.erzeugeGegenstaende(1)
        zeichenManager.zeichenObjekte = self.ziele

        self.hauptschleife()
        self.spiel_fenster.mainloop()

if(__name__=="__main__"):
    spiel()