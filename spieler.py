import tkinter

GRAFIK_SPIELER = "spieler.png"

class spieler:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        #Lege die Position fest, an die das Objekt bewegt werden soll
        self.zielX = self.x
        self.zielY = self.y

        bilddatei = GRAFIK_SPIELER
        self.bild = tkinter.PhotoImage(file=bilddatei)

        self.hoehe = self.bild.height()
        self.breite = self.bild.width()

        self.zeichnung = None

    def aktualisiere(self, maluntergrund):
        if(self.zeichnung == None):
            self.zeichnung = maluntergrund.create_image(self.x, self.y, 
                                                     image=self.bild)
        else:
            delta_x = self.zielX - self.x
            delta_y = self.zielY - self.y
            maluntergrund.move(self.zeichnung, delta_x, delta_y)

            self.x = self.zielX
            self.y = self.zielY

    def setzePosition(self, x, y):
        self.zielX = x
        self.zielY = y