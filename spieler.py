import tkinter
import spielfeld

GRAFIK_SPIELER = "spieler.png"
START_X = 60
START_Y = spielfeld.HOEHE / 2

class Spieler:
    def __init__(self, leinwand):
        """Instanziiere

        Argumente:
        leinwand -- Die Leinwand, auf die die Grafiken gezeichnet werden.
        """
        # Initialisiere Variablen
        self.leinwand = leinwand
        self.x = START_X
        self.y = START_Y
        self.zielX = self.x
        self.zielY = self.y
        # Lade die Grafik
        bilddatei = GRAFIK_SPIELER
        self.grafik = tkinter.PhotoImage(file=bilddatei)
        self.zeichnung = None
        # Verwende die Hoehe und Breite der Grafik als Objektgroessen
        self.hoehe = self.grafik.height()
        self.breite = self.grafik.width()

    def reset(self):
        """Setze auf die Ausgangswerte zurück. Wird bei einem Neustart
        des Spiels aufgerufen.
        """
        self.zielX = START_X
        self.zielY = START_Y

    def aktualisiere(self):
        """Zeichnet das Objekt auf die Leinwand."""
        if(self.zeichnung == None):
            self.zeichnung = self.leinwand.create_image(self.x, self.y, 
                                                     image=self.grafik)
        delta_x = self.zielX - self.x
        delta_y = self.zielY - self.y
        self.leinwand.move(self.zeichnung, delta_x, delta_y)

        self.x = self.zielX
        self.y = self.zielY

    def setzePosition(self, x, y):
        """Legt die Position des Objektes fest."""
        self.zielX = x
        self.zielY = y

    def abgrenzung(self):
        """Gibt die Abgrenzungen des Objektes als Woerterbuch zurueck."""
        return dict([('x', self.x), ('y', self.y),
                    ('hoehe', self.hoehe), ('breite', self.breite)])