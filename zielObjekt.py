import random
import os
import tkinter

GRAFIKEN_STEIN = ["stein0.png", "stein1.png", "stein2.png",]
GRAFIK_TREIBSTOFF = "treibstoff.png"

STEIN = 0
TREIBSTOFF = 1

GESCHWINDIGKEIT = 3

class ZielObjekt:
    def __init__(self, leinwand, x, y, typ):
        """Instanziiere

        Argumente:
        leinwand -- Die Leinwand, auf die die Grafiken gezeichnet werden.
        x -- x-Position
        y -- y-Position
        typ -- Typ des Objektes
        """
        # Initialisiere Variablen 
        self.leinwand = leinwand
        self.x = x
        self.y = y
        self.typ = typ
        self.valide = True
        self.delta_x = 0
        # Wähle die zu verwendende Grafik entsprechend dem Typ aus
        if(self.typ == STEIN):
            bilddatei = GRAFIKEN_STEIN[random.randint(0,
                                                      len(GRAFIKEN_STEIN) - 1)]
        elif(self.typ == TREIBSTOFF):
            bilddatei = GRAFIK_TREIBSTOFF
        # Lade die Grafik
        self.grafik = tkinter.PhotoImage(file=bilddatei)
        self.zeichnung = self.leinwand.create_image(self.x, self.y, 
                                                    image=self.grafik)
        # Verwende die Hoehe und Breite der Grafik als Objektgroessen
        self.hoehe = self.grafik.height()
        self.breite = self.grafik.width()

    def aktualisiere(self):
        """Zeichnet das Objekt auf die Leinwand."""
        self.leinwand.move(self.zeichnung, self.delta_x, 0)
        self.x += self.delta_x
        self.delta_x = 0

    def bewegeDich(self):
        """Verschiebe die x-Koordinate um distanz nach links und makriere das
        Objekt als ungültig, falls es das Spielfeld verlässt.
        """
        self.delta_x -= GESCHWINDIGKEIT
        if(self.x + self.delta_x <= 0):
            self.valide = False

    def abgrenzung(self):
        """Gibt die Abgrenzungen des Objektes als Woerterbuch zurueck."""
        return dict([('x', self.x), ('y', self.y),
                    ('hoehe', self.hoehe), ('breite', self.breite)])