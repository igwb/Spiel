class spieler:
    def __init__(self, x=60, y=0, breite=45, hoehe=45):
        self.x = x
        self.y = y
        self.breite = breite
        self.hoehe = hoehe

        self.zeichnung = None

    def zeichne(self, malflaeche):
        #Lösche die vorherige Zeichnung von der malflaeche und fertige eine
        #neue an.
        malflaeche.delete(self.zeichnung)
        
        self.zeichnung = malflaeche.create_rectangle(self.x, self.y,
                                                     self.x + self.breite,
                                                     self.y + self.hoehe,
                                                     fill="#00ff00",
                                                     outline="#0000ff")