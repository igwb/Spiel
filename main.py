import time
import tkinter
import gegenstand
import zeichenManager

def initialize():
    #Bereite globale Variablen für das Fenster und die Spielfläche vor
    global spiel_fenster
    global spiel_feld
    #Bereite globale Variablen für den Spieler und die Ziele vor
    global spieler
    global ziele
    #Lege das FPS(Frames per second)-limit fest
    global gewuenschteFPS
    gewuenschteFPS = 60

    #Erstelle das Programmfenster und lege seine Größe fest.
    spiel_fenster = tkinter.Tk()
    spiel_fenster.resizable(width=False, height=False)
    spiel_fenster.geometry("600x400")

    #Erstelle das Spielfeld und lege seine Größe fest.
    spiel_feld = tkinter.Canvas(width=600,height=300)

    #Zeichne den Spielfeldhintergrund
    spiel_feld.create_rectangle(0, 0, 600, 300, fill="#000",outline="")
    spiel_feld.pack()

def update():
    for ziel in ziele:
        ziel.bewegeDich(1)

    zeichne()
    spiel_fenster.after(1, update)

def zeichne():
    print("zeichnet")
    zeichenManager.zeichne(spiel_feld)


def hauptschleife():
    print("spiel gestartet")
    letzter_zeitpunkt = time.time()

    spiel_fenster.after(1, update)
    spiel_fenster.mainloop()

def erzeugeGegenstaende(anzahl):
    erzeugteObjekte = []

    for i in range(anzahl):
        erzeugteObjekte.append(gegenstand.gegenstand())
    return erzeugteObjekte

global spiel_fenster
global spiel_feld

ziele = erzeugeGegenstaende(1)
zeichenManager.zeichenObjekte = ziele

if(__name__=="__main__"):
    initialize()
    print(spiel_fenster)
    spiel_laeuft = True
    hauptschleife()
