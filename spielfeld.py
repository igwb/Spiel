import tkinter

class Konst:
    """Beinhaltet wichtige Konstanten"""

    SPIELFELD_HOEHE = 250
    SPIELFELD_BREITE = 600
    SPIELFELD_HINTERGRUND = "hintergrund2.png"

    HINTERGRUND_GESCHWINDIGKEIT = 1


class Spielfeld:
    def __init__(self):

        #Erstelle das Spielfeld und lege seine Größe fest.
        self.maluntergrund = tkinter.Canvas(height=Konst.SPIELFELD_HOEHE)
        
        #Nutze die volle Fensterbreite
        self.maluntergrund.pack(fill="x")

        self.hintergrundbild = tkinter.PhotoImage(file=
                                                  Konst.SPIELFELD_HINTERGRUND)
        self.hintergrund_links = None
        self.hintergrund_rechts = None
        self.hintergrund_x = 0

    def zeichneHintergrund(self):
        if(self.hintergrund_links == None):
           self.hintergrund_links = self.maluntergrund.create_image(
                                                self.hintergrund_x, 
                                                0, image=self.hintergrundbild,
                                                anchor="nw")
        if(self.hintergrund_rechts == None):
            self.hintergrund_rechts = self.maluntergrund.create_image(
                                        self.hintergrund_x +
                                        self.hintergrundbild.width(),
                                        0, image=self.hintergrundbild,
                                        anchor="nw")



        self.hintergrund_x -= Konst.HINTERGRUND_GESCHWINDIGKEIT
        if(self.hintergrund_x <= 0 - self.hintergrundbild.width()):
            self.hintergrund_x += self.hintergrundbild.width()
            delta_x = self.hintergrundbild.width()
        else:
            delta_x = Konst.HINTERGRUND_GESCHWINDIGKEIT * -1

        self.maluntergrund.move(self.hintergrund_links, delta_x, 0)
        self.maluntergrund.move(self.hintergrund_rechts, delta_x, 0)




