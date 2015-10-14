import tkinter

class spieler:
    def __init__(self, x, y, bild):
        self.x = x
        self.y = y

        #Lege die Position fest, an die das Objekt bewegt werden soll
        self.zielX = self.x
        self.zielY = self.y

        self.hoehe = bild.height()
        self.breite = bild.width()

        self.bild = bild
        self.zeichnung = None

    def aktualisiere(self, malflaeche):
        if(self.zeichnung == None):
            self.zeichnung = malflaeche.create_image(self.x, self.y, 
                                                     image=self.bild)
        else:
            malflaeche.move(self.zeichnung, self.zielX - self.x,
                                    self.zielY - self.y)

            self.x = self.zielX
            self.y = self.zielY

    def setzePosition(self, x, y):
        self.zielX = x
        self.zielY = y