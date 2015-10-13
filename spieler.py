class spieler:
    def __init__(self):
        self.x = 60
        self.y = 0
        self.zeichnung = None

    def zeichne(self, malflaeche):
        #Lösche die vorherige Zeichnung von der malflaeche und fertige eine
        #neue an.
        malflaeche.delete(self.zeichnung)
        
        self.zeichnung = malflaeche.create_rectangle(self.x, self.y,
                                                     self.x + 45,
                                                     self.y + 45,
                                                     fill="#00ff00",
                                                     outline="")