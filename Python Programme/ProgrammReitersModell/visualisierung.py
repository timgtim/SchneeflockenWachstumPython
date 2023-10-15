import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import matplotlib.colors as mcolors
import time, os, csv



def visualisierung(dateiname, bildsichern = True, bildauflösung = 300, hellefarbe='#ADD8E6', dunklefarbe='#0019a6'):
    pfad = 'ProgrammReitersModell/Dateien/csvDateien/'
    os.system('clear')
    while True:
        try:
            csv_datei = pfad + dateiname
            with open(csv_datei, 'r'):  # Versucht Datei zu öffnen
                break  
        
        except FileNotFoundError:
            os.system('clear')
            print('Keine Datei mit diesem Namen gefunden.')
            dateiname = str(input('Dateiname ohne Ordner und Endung: '))

    start = time.time()
    x_liste = []
    y_liste = []
    z_liste = []

    with open(csv_datei, 'r') as datei:
        csv_reader = csv.reader(datei)
        erste_zeile = next(csv_reader, None)

    alpha = erste_zeile[1]
    beta = erste_zeile[3]
    gamma = erste_zeile[5]

    # Daten aus der CSV-Datei lesen
    with open(csv_datei, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            try:
                x, y, z = line.strip().split(',')
                x = float(x) 
                y = float(y)
                if y%2 != 0: #Koordinaten richtig anordnen, versetzte Spalten
                    x = x + 0.5
                y = y * 3**0.5/2
                
                x *= 3**0.5
                y *= 3**0.5
            
                x_liste.append(float(x))
                y_liste.append(float(y))
                z_liste.append(float(z))
            except:
                pass
            
                
    csv_zeit = time.time() - start
    start = time.time()

    multiplikator = 100/max(z_liste) 
    for i in range(len(z_liste)):
        z_liste[i] = int(z_liste[i]*multiplikator)

    # Erstellen eines Farbverlaufs von Hellblau zu Dunkelblau
    colors = [str(hellefarbe), str(dunklefarbe)]

    # Erstellen eines Colormap-Objekts
    cmap = mcolors.LinearSegmentedColormap.from_list('Blau', colors, N=100)


    #Hexagone an Koordinaten zeichnen
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')
    

    for x, y, z in zip(x_liste, y_liste, z_liste):
        farbe = cmap(z)  # Farbe basierend auf dem normierten Wert z erhalten
        hex = RegularPolygon((x, y), numVertices=6, radius=1, alpha=1, edgecolor=farbe, facecolor=farbe)
        ax.add_patch(hex)

    #ax.set_xlim(-zeilen*0.01, zeilen*3**0.5+zeilen*0.01)  
   # ax.set_ylim(-zeilen*0.01, zeilen*1.5+zeilen*0.01) 
    plt.xlabel('X-Koordinate')
    plt.ylabel('Y-Koordinate')
    plt.title(f'Schneeflocke mit alpha={alpha}, beta={beta}, gamma={gamma}')


    grafik_zeit = time.time() - start
    plt.autoscale(enable = True)
    if bildsichern == True:
        plt.savefig('ProgrammReitersModell/Dateien/Bilder/' + str(dateiname[:-4]) + '-bild.png', dpi=bildauflösung)
    plt.show()


    os.system('clear')
    print(len(x_liste), ' Zellen')
    print('''
Zeit CSV:''', csv_zeit, '''
Grafik Zeit:''', grafik_zeit )
    beenden = input()
    
    return csv_datei


def bilderFürGif(ordnerCSV, auflösung=500):
    auflösung = 500 #Auflösung für gif-Bilder
    farbehell = '#bfc7ff'
    farbedunkel = '#0000b5'
    gifcounter = 0
    z_Werte = []
    ordnerBilder = ordnerCSV[:-9] + 'BilderGif'  
    if not os.path.exists(ordnerBilder): #wenn es keinen Ordner mit dem Namen gibt, einen neuen erstellen
        os.makedirs(ordnerBilder)
    datei_pfad = ordnerCSV + '/gif1.csv'
    with open(datei_pfad, 'r') as datei:
        csv_reader = csv.reader(datei)
        erste_zeile = next(csv_reader, None)

        alpha = erste_zeile[1]
        beta = erste_zeile[3]
        gamma = erste_zeile[5]
        zeilen = int(erste_zeile[7])


    

    for y in os.listdir(ordnerCSV): #jede datei in Ordner durchgehen
        gifcounter += 1
        datei_pfad = ordnerCSV + '/gif' + str(gifcounter) + '.csv'

        while True:
            try:
                with open(datei_pfad, 'r'):  # Versucht Datei zu öffnen
                    break  
            except FileNotFoundError:
                print('Keine Datei mit diesem Namen gefunden.')

        start = time.time()
        x_liste = []
        y_liste = []
        z_liste = []

        # Daten aus der CSV-Datei lesen
        with open(datei_pfad, 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:  
                x, y, z = line.strip().split(',')
                x = float(x) 
                y = float(y)
                if y%2 != 0: #Koordinaten richtig anordnen, versetzte Spalten
                    x = x + 0.5
                y = y * 3**0.5/2
                
                x *= 3**0.5 
                y *= 3**0.5 
                
                x_liste.append(float(x))
                y_liste.append(float(y))
                z_liste.append(float(z))
                
        multiplikator = 99.9/max(z_liste) #grösster Wert von Farben = 100
        for i in range(len(z_liste)):
            z_liste[i] = int(z_liste[i]*multiplikator)

        # Erstellen von einem Farbverlauf
        colors = [farbehell, farbedunkel]
        cmap = mcolors.LinearSegmentedColormap.from_list('Blues', colors, N=100)


        csv_zeit = time.time() - start
        start = time.time()


        #Hexagone an Koordinaten zeichnen
        fig, ax = plt.subplots(1, frameon=True)
        ax.set_aspect('equal')
        ax.set_xlim(-zeilen*0.05, zeilen*3**0.5+zeilen*0.02)  
        ax.set_ylim(-zeilen*0.05, zeilen*1.5+zeilen*0.05)  
      


        for x, y, z in zip(x_liste, y_liste, z_liste):
            farbe = cmap(z)  # Farbe basierend auf dem normierten Wert z erhalten
            hex = RegularPolygon((x, y), numVertices=6, radius=1, alpha=1, edgecolor=farbe, facecolor=farbe)
            ax.add_patch(hex)
            
        plt.xlabel('X-Koordinate')
        plt.ylabel('Y-Koordinate')
        plt.title(f'Schneeflocke mit alpha={alpha}, beta={beta}, gamma={gamma}')


        grafik_zeit = time.time() - start

        plt.savefig(str(ordnerCSV[:-9]) + 'BilderGif/' + str(gifcounter) + '.png', dpi=auflösung)


    os.system('clear')
    print('''
    Zeit CSV:''', csv_zeit, '''
    Grafik Zeit:''', grafik_zeit )


if __name__ == '__main__':
    visualisierung('abbildung.csv', True)