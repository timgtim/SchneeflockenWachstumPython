import simulation, visualisierung, gif, os

os.system('Clear')

print('''
Simulation und Visualisierung von Reiters Modell zum Schneeflockenwachstum:''')
x = True
while x:
    eingabe = input('''
(1) - Schneeflocke berechnen und visualisieren, wird nicht gespeichert
(2) - Schneeflocke berechnen und speichern
(3) - Animation von Schneeflockenwachstum erstellen
(4) - Bereits existierende Datei visualisieren
                    
Wähle 1, 2, 3 oder 4: ''')
    os.system('clear')

    if eingabe == '1' or eingabe == '2' or eingabe == '3' or eingabe == '4': 
        x = False
    



if eingabe == '1':
    Zzeilen = int(input('Anzahl Zellen in einer Zeile: '))
    Aalpha = float(input('Alpha:'))
    Bbeta = float(input('Beta: '))
    Ggamma = float(input('Gamma: '))

    os.remove(visualisierung.visualisierung(simulation.main(Zzeilen, Aalpha, Bbeta, Ggamma), False))

elif eingabe == '2':
    Zzeilen = int(input('Anzahl Zellen in einer Zeile: '))
    Aalpha = float(input('Alpha:'))
    Bbeta = float(input('Beta: '))
    Ggamma = float(input('Gamma: '))

    dateiname = simulation.main(Zzeilen, Aalpha, Bbeta, Ggamma)
    nameändern = input('''
                       
(1) - Eigener Dateiname festlegen
(2) - Standardname behalten                   
''')
    if nameändern == '1':
        neuername = input('Neuer Dateiname: ')
        neuername = neuername + '.csv'
        os.rename('ProgrammReitersModell/Dateien/csvDateien/'+ dateiname, 'ProgrammReitersModell/Dateien/csvDateien/' + neuername)
    else:
        neuername = dateiname
    bild = input('''
Soll die erstellte Schneeflocke als Bild gesichert werden?

(1) - Ja
(2) - Nein 
''')
    
    if bild == '1':
        bild = True
    else:
        bild = False

    visualisierung.visualisierung(neuername, bild)

elif eingabe == '3':
    Zzeilen = int(input('Anzahl Zellen in einer Zeile: '))
    Aalpha = float(input('Alpha:'))
    Bbeta = float(input('Beta: '))
    Ggamma = float(input('Gamma: '))

    gifAbstand = int(input('Nach wie vielen neuen Zellreihen soll ein neues Bild für die Animation erstellt werden: '))

    ordnerName = simulation.mainFürGif(Zzeilen, Aalpha, Bbeta, Ggamma, gifAbstand)
    visualisierung.bilderFürGif(ordnerName)
    gif.gifErstellen(ordnerName[:-9] + 'BilderGif')

elif eingabe == '4':
    datei = input('''
Dateiname von Schneeflocke, die Visualisiert werden soll:''')
    bild = input('''
Soll die erstellte Schneeflocke als Bild gesichert werden?

(1) - Ja
(2) - Nein 
''')
    
    if bild == '1':
        bild = True
    else:
        bild = False

    datei = datei + '.csv'
    visualisierung.visualisierung(datei, bild, 300)