import random
import os
import tkinter

GRAFIKEN_STEIN = ["stein0.png", "stein1.png", "stein2.png"]
GRAFIK_TREIBSTOFF = "treibstoff.png"

STEIN = 0
TREIBSTOFF = 1

class zielObjekt:
    def __init__(self, maluntergrund, x, y, typ, ):
        #Initialisiere Variablen 
        self.maluntergrund = maluntergrund
        self.x = x
        self.y = y
        self.typ = typ

        self.valide = True
        self.delta_x = 0

        #Wähle die zu verwendende Grafik entsprechend dem Typ aus
        if(self.typ == STEIN):
            bilddatei = GRAFIKEN_STEIN[random.randint(0,
                                                      len(GRAFIKEN_STEIN) - 1)]
        elif(self.typ == TREIBSTOFF):
            bilddatei = GRAFIK_TREIBSTOFF

        self.grafik = tkinter.PhotoImage(file=bilddatei)
        self.zeichnung = self.maluntergrund.create_image(self.x, self.y, 
                                                         image=self.grafik)

        self.hoehe = self.grafik.height()
        self.breite = self.grafik.width()

    def aktualisiere(self):
        self.maluntergrund.move(self.zeichnung, self.delta_x, 0)
        self.x += self.delta_x
        self.delta_x = 0

    def bewegeDich(self, distanz):
        #Verschiebe die x-Koordinate um distanz nach links und makriere das
        #Objekt als ungültig, falls es das Spielfeld verlässt
        self.delta_x -= distanz
        if(self.x + self.delta_x <= 0):
            self.valide = False
