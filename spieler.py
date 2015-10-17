import tkinter

GRAFIK_SPIELER = "spieler.png"

class spieler:
    def __init__(self, maluntergrund, x, y):
        #Initialisiere Variablen
        self.maluntergrund = maluntergrund
        self.x = x
        self.y = y
        #Lege die Position fest, an die das Objekt bewegt werden soll
        self.zielX = self.x
        self.zielY = self.y

        #Lade die Grafik
        bilddatei = GRAFIK_SPIELER
        self.grafik = tkinter.PhotoImage(file=bilddatei)
        self.zeichnung = None

        self.hoehe = self.grafik.height()
        self.breite = self.grafik.width()

    def aktualisiere(self):
        if(self.zeichnung == None):
            self.zeichnung = self.maluntergrund.create_image(self.x, self.y, 
                                                     image=self.grafik)
        delta_x = self.zielX - self.x
        delta_y = self.zielY - self.y
        self.maluntergrund.move(self.zeichnung, delta_x, delta_y)

        self.x = self.zielX
        self.y = self.zielY

    def setzePosition(self, x, y):
        self.zielX = x
        self.zielY = y