class zielObjekt:
   
    QUADRAT = 0
    DREIECK = 1
    KREIS = 2

    def __init__(self):
        self.farbe = "#f5f"
        self.groesse = 30
        self.x = 500
        self.y = 50
        self.zeichnung = None
        self.valide = True

    def zeichne(self, malflaeche):
        #Lösche die vorherige Zeichnung von der malflaeche und fertige eine
        #neue an.
        malflaeche.delete(self.zeichnung)
        self.zeichnung = malflaeche.create_rectangle(self.x, self.y,
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