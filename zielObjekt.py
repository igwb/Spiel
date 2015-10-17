import random
import os
import tkinter

GRAFIKEN_STEIN = ["stein0.png", "stein1.png", "stein2.png"]
GRAFIK_TREIBSTOFF = ["treibstoff.png"]

STEIN = 0
TREIBSTOFF = 1

class zielObjekt:
    def __init__(self, x, y, typ, maluntergrund):
        self.x = x
        self.y = y

        #Lege die Position fest, an die das Objekt bewegt werden soll
        self.zielX = self.x
        self.zielY = self.y

        self.valide = True
        self.typ = typ

        self.maluntergrund = maluntergrund
        self.zeichnung = None

        #Wähle die zu verwendende Grafik entsprechend dem Typ aus
        if(self.typ == STEIN):
            bilddatei = GRAFIKEN_STEIN[random.randint(0,
                                                      len(GRAFIKEN_STEIN) - 1)]
        elif(self.typ == TREIBSTOFF):
            bilddatei = GRAFIK_TREIBSTOFF

        self.bild = tkinter.PhotoImage(file=bilddatei)

        self.hoehe = self.bild.height()
        self.breite = self.bild.width()

    def aktualisiere(self):
        if(self.zeichnung == None):
            self.zeichnung = self.maluntergrund.create_image(self.x, self.y, 
                                                             image=self.bild)

        delta_x = self.zielX - self.x
        delta_y = self.zielY - self.y
        self.maluntergrund.move(self.zeichnung, delta_x, delta_y)

        self.x = self.zielX
        self.y = self.zielY

    def bewegeDich(self, distanz):
        #Verschiebe die x-Koordinate um distanz nach links und makriere das
        #Objekt als ungültig, falls es das Spielfeld verlässt
        self.zielX -= distanz
        if(self.zielX <= 0):
            self.valide = False
