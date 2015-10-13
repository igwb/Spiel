import random

class zielObjekt:
   
    QUADRAT = 0
    KREIS = 1

    def __init__(self):
        self.farbe = "#d32a79"
        self.groesse = 30
        self.x = 500
        self.y = 50
        self.zeichnung = None
        self.valide = True
        self.typ = random.randint(0,1)

    def zeichne(self, malflaeche):
        #Lösche die vorherige Zeichnung von der malflaeche und fertige eine
        #neue an.
        malflaeche.delete(self.zeichnung)

        if(self.typ == self.QUADRAT):
            self.zeichnung = malflaeche.create_rectangle(self.x, self.y,
                                                     self.x + self.groesse,
                                                     self.y + self.groesse,
                                                     fill=self.farbe,
                                                     outline="")
        elif(self.typ == self.KREIS):
            self.zeichnung = malflaeche.create_oval(self.x, self.y,
                                                     self.x + self.groesse,
                                                     self.y + self.groesse,
                                                     fill=self.farbe,
                                                     outline="")          

    def bewegeDich(self, distanz):
        #Verschiebe die x-Koordinate um distanz nach links und makriere das
        #Objekt als ungültig, falls es das Spielfeld verlässt
        self.x -= distanz
        if(self.x <= 0):
            self.valide = False