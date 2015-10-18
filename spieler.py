import tkinter
import spielfeld

GRAFIK_SPIELER = "spieler2.png"
START_X = 60
START_Y = spielfeld.HOEHE / 2

class spieler:
    def __init__(self, maluntergrund):
        #Initialisiere Variablen
        self.maluntergrund = maluntergrund
        self.reset()

        self.x = START_X
        self.y = START_Y


        #Lade die Grafik
        bilddatei = GRAFIK_SPIELER
        self.grafik = tkinter.PhotoImage(file=bilddatei)
        self.zeichnung = None

        self.hoehe = self.grafik.height()
        self.breite = self.grafik.width()

    def reset(self):
        

        #Lege die Position fest, an die das Objekt bewegt werden soll
        self.zielX = START_X
        self.zielY = START_Y

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