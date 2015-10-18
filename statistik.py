import tkinter
import zielObjekt
import spiel

TREIBSTOFFANZEIGE_HOEHE = 20
TREIBSTOFFANZEIGE_FARBE = "#ff00ff"

PUNKTEANZEIGE_HOEHE = 20
PUNKTEANZEIGE_HINTERGRUNDFARBE = "#000000"
PUNKTEANZEIGE_TEXTFARBE = "#ffffff"

START_PUNKTZAHL = 0
START_TREIBSTOFF = 100

class Statistik:
    def __init__(self):
        """Instanziiere"""
        # Initialisiere Variablen
        self.zeichnung_treibstoff = None
        self.punkte = START_PUNKTZAHL
        self.treibstoff = START_TREIBSTOFF
        # Erstelle die Treibstoffanzeige
        self.leinwand = tkinter.Canvas(height=TREIBSTOFFANZEIGE_HOEHE)
        # Nutze die volle Fensterbreite
        self.leinwand.pack(fill="x")
        # Erstelle die Punkteanzeige
        self.text_punkte = tkinter.StringVar()
        self.text_punkte.set("0")
        self.label_punkte = tkinter.Label(height=PUNKTEANZEIGE_HOEHE,
                                          bg=PUNKTEANZEIGE_HINTERGRUNDFARBE,
                                          fg=PUNKTEANZEIGE_TEXTFARBE,
                                          textvariable=self.text_punkte,
                                          font=("Arial", 20))
        # Nutze die volle Fensterbreite
        self.label_punkte.pack(fill="x")

    def reset(self):
        """Setze auf die Ausgangswerte zurück. Wird bei einem Neustart
        des Spiels aufgerufen.
        """
        self.punkte = START_PUNKTZAHL
        self.treibstoff = START_TREIBSTOFF

    def zielGesammelt(self, ziel):
        """Aktualisiere die Statistik entsprechend dem gesammelten Ziel

        Argumente:
        ziel -- das eingesammelte Ziel
        """
        if(ziel.typ == zielObjekt.STEIN):
            self.treibstoff -= 5
            self.punkte -= 5
        elif(ziel.typ == zielObjekt.TREIBSTOFF):
            self.treibstoff = min([self.treibstoff + 5, START_TREIBSTOFF])
            self.punkte += 3

    def verbraucheTreibstoff(self, menge):
        """Reduziert den Treibstoffvorrat um menge."""
        self.treibstoff -= menge

    def erhoehePunktzahl(self, punkte):
        """Erhoeht die Punktzahl um punkte."""
        self.punkte += punkte

    def aktualisiere(self):
        """Zeichnet das Objekt."""
        # Zeichne die Treibstoffanzeige
        self.leinwand.delete(self.zeichnung_treibstoff)
        self.zeichnung_treibstoff = self.leinwand.create_rectangle(0, 0,
                                                int(spiel.FENSTER_BREITE * 
                                                    (self.treibstoff / 100)),
                                                TREIBSTOFFANZEIGE_HOEHE,
                                                fill=TREIBSTOFFANZEIGE_FARBE,
                                                outline="")
        # Aktualisiere die Punkteanzeige, das Neuzeichnen uebernimmt tkinter.
        self.text_punkte.set(str(int(self.punkte)))