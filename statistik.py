import tkinter
import zielObjekt

TREIBSTOFFANZEIGE_HOEHE = 20
TREIBSTOFFANZEIGE_BREITE = 600
TREIBSTOFFANZEIGE_FARBE = "#ff00ff"

PUNKTEANZEIGE_HOEHE = 20
PUNKTEANZEIGE_BREITE = 600
PUNKTEANZEIGE_HINTERGRUNDFARBE = "#000000"
PUNKTEANZEIGE_TEXTFARBE = "#ffffff"

class Statistik:
    def __init__(self):
        #Initialisiere Variablen
        self.zeichnung_treibstoff = None
        self.punkte = 0
        self.treibstoff = 100

        #Erstelle die Treibstoffanzeige
        self.maluntergrund = tkinter.Canvas(width=TREIBSTOFFANZEIGE_BREITE,
                                            height=TREIBSTOFFANZEIGE_HOEHE)
        self.maluntergrund.pack()
        #Erstelle die Punkteanzeige
        self.text_punkte = tkinter.StringVar()
        self.text_punkte.set("0")
        self.label_punkte = tkinter.Label(height=PUNKTEANZEIGE_HOEHE,
                                          bg=PUNKTEANZEIGE_HINTERGRUNDFARBE,
                                          fg=PUNKTEANZEIGE_TEXTFARBE,
                                          textvariable=self.text_punkte,
                                          font=("Arial", 20))
        #Nutze die volle Fensterbreite
        self.label_punkte.pack(fill="x")

    def zielGesammelt(self, ziel):
        if(ziel.typ == zielObjekt.STEIN):
            self.treibstoff -= 1
        elif(ziel.typ == zielObjekt.TREIBSTOFF):
            self.treibstoff = min([self.treibstoff + 5, 100])
            self.punkte += 3

    def verbraucheTreibstoff(self, menge):
        self.treibstoff -= menge

    def erhoehePunktzahl(self, punkte):
        self.punkte += punkte

    def aktualisiere(self):
        #Zeichne die Treibstoffanzeige
        self.maluntergrund.delete(self.zeichnung_treibstoff)
        self.zeichnung_treibstoff = self.maluntergrund.create_rectangle(0, 0,
                                                int(TREIBSTOFFANZEIGE_BREITE * 
                                                    (self.treibstoff / 100)),
                                                TREIBSTOFFANZEIGE_HOEHE,
                                                fill=TREIBSTOFFANZEIGE_FARBE,
                                                outline="")
        #Aktualisiere die Punkteanzeige, das Neuzeichnen übernimmt tkinter.
        self.text_punkte.set(str(int(self.punkte)))