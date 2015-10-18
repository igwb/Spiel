import tkinter

HOEHE = 250
HINTERGRUND = "hintergrund.png"

HINTERGRUND_GESCHWINDIGKEIT = 1

class Spielfeld:
    def __init__(self):
        """Instanziiere"""
        # Initialisiere Variablen
        self.hintergrund_links = None
        self.hintergrund_rechts = None
        self.hintergrund_x = 0

        # Erstelle das Spielfeld und lege seine Größe fest.
        self.leinwand = tkinter.Canvas(height=HOEHE)
        # Nutze die volle Fensterbreite
        self.leinwand.pack(fill="x")
        # Lade das Hintergrundbild
        self.hintergrundbild = tkinter.PhotoImage(file=HINTERGRUND)

    def zeichneHintergrund(self):
        """Zeichne den Spielfeldhintergrund."""
        # Zeichne die Grafiken, falls noetig.
        if(self.hintergrund_links == None):
           self.hintergrund_links = self.leinwand.create_image(
                                                self.hintergrund_x, 
                                                0, image=self.hintergrundbild,
                                                anchor="nw")
        if(self.hintergrund_rechts == None):
            self.hintergrund_rechts = self.leinwand.create_image(
                                                self.hintergrund_x +
                                                self.hintergrundbild.width(),
                                                0, image=self.hintergrundbild,
                                                anchor="nw")

        # Aktualisiere die Hintergrundposition
        self.hintergrund_x -= HINTERGRUND_GESCHWINDIGKEIT
        if(self.hintergrund_x <= 0 - self.hintergrundbild.width()):
            self.hintergrund_x += self.hintergrundbild.width()
            delta_x = self.hintergrundbild.width()
        else:
            delta_x = HINTERGRUND_GESCHWINDIGKEIT * -1
        # Bewege die Hintergrundteilstuecke
        self.leinwand.move(self.hintergrund_links, delta_x, 0)
        self.leinwand.move(self.hintergrund_rechts, delta_x, 0)




