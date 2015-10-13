import random

farbkatalog= ["#e81b7b", "#15c1c1", "#b20e42"]

def erzeugeZiel(minX, maxX, minY, maxY, groesse=None, farbe=None, typ=None):

    x = random.randint(minX, maxX)
    y = random.randint(minY, maxY)

    if(groesse == None):
        groesse = random.randint(15,25)

    if(farbe == None):
        farbe = farbkatalog[random.randint(0,len(farbkatalog) - 1)]

    if(typ == None):
        typ = random.randint(0,1)

    return zielObjekt(x, y, groesse, farbe, typ)


class zielObjekt:
   
    QUADRAT = 0
    KREIS = 1

    def __init__(self,x,y,groesse,farbe,typ):
        self.farbe = farbe
        self.groesse = groesse
        self.x = x
        self.y = y
        self.zeichnung = None
        self.valide = True
        self.typ = typ

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
