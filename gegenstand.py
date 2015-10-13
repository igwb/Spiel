class gegenstand:
   
    QUADRAT = 0
    DREIECK = 1
    KREIS = 2

    def __init__(self):
        self.farbe = "#f5f"
        self.groesse = 30
        self.x = 500
        self.y = 50
        self.zeichnung = None

    def zeichne(self, malflaeche):

        malflaeche.delete(self.zeichnung)
        self.zeichnung = malflaeche.create_rectangle(self.x, self.y,
                                                     self.x + self.groesse,
                                                     self.y + self.groesse,
                                                     fill=self.farbe,
                                                     outline="")

    def bewegeDich(self, distanz):
        #Verschiebe die x-Koordinate um distanz nach links und lösche
        #diese Instanz, wenn sie sich außerhalb des Spielfeldes befindent.
        self.x -= distanz
        print(self.x)
        if(self.x - self.groesse <= 0):
            del(self)