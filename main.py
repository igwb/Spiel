import time


gewuenschteFPS=60
spiel_laeuft=False

def update():

    pass

def zeichne():
    pass

def hauptschleife():

    letzter_zeitpunkt=time.time()

    while (spiel_laeuft):
        
        jetzt=time.time()

        update()
        zeichne()

        schlaf_laenge= 1./gewuenschteFPS - (jetzt - letzter_zeitpunkt)/1000
        letzter_zeitpunkt=jetzt

        if(schlaf_laenge > 0):
            time.sleep(schlaf_laenge)


spiel_laeuft=True
hauptschleife()