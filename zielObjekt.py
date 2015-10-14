import random

farbkatalog = ["#e81b7b", "#15c1c1", "#b20e42"]

def erzeugeZiel(minX, maxX, minY, maxY, maluntergrund, 
                groesse=None, farbe=None, typ=None):

    x = random.randint(minX, maxX)
    y = random.randint(minY, maxY)

    if(groesse == None):
        groesse = random.randint(15,25)

    if(farbe == None):
        farbe = farbkatalog[random.randint(0,len(farbkatalog) - 1)]

    if(typ == None):
        typ = random.randint(0,1)

    return zielObjekt(x, y, groesse, farbe, typ, maluntergrund)


class zielObjekt:
    QUADRAT = 0
    KREIS = 1

    def __init__(self, x, y, groesse, farbe, typ, maluntergrund):
        self.farbe = farbe
        self.groesse = groesse

        self.x = x
        self.y = y

        #Lege die Position fest, an die das Objekt bewegt werden soll
        self.zielX = self.x
        self.zielY = self.y

        self.maluntergrund = maluntergrund

        self.zeichnung = None
        self.valide = True
        self.typ = typ

    def aktualisiere(self):

        if(self.zeichnung == None):
            if(self.typ == self.QUADRAT):
                self.zeichneQuadrat()
            elif(self.typ == self.KREIS):
                self.zeichneKreis()

        self.maluntergrund.move(self.zeichnung,self.zielX - self.x,
                                self.zielY - self.y)

        self.x = self.zielX
        self.y = self.zielY

    
    def zeichneQuadrat(self):
        self.zeichnung = self.maluntergrund.create_rectangle(self.x, self.y,
                                                     self.x + self.groesse,
                                                     self.y + self.groesse,
                                                     fill=self.farbe,
                                                     outline="")
    def zeichneKreis(self):
        self.zeichnung = self.maluntergrund.create_oval(self.x, self.y,
                                                    self.x + self.groesse,
                                                    self.y + self.groesse,
                                                    fill=self.farbe,
                                                    outline="")      


    def bewegeDich(self, distanz):
        #Verschiebe die x-Koordinate um distanz nach links und makriere das
        #Objekt als ungültig, falls es das Spielfeld verlässt
        self.zielX -= distanz
        if(self.zielX <= 0):
            self.valide = False
