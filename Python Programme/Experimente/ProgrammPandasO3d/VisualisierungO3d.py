import open3d as o3d
import numpy as np
import os, csv, time


w3d2 = np.sqrt(3)/2
linien = np.array([[0, 0],])
corners = np.array([[0, 0, 0],])
anzahl_zeilen = 0

def newCorners(sPx, sPy): #Startpunkt x und y, werden aus CSV Datei ausgelesen
    global corners, w3d2

    eckpunkte = [
    [0.5, w3d2],
    [1, 0],
    [0.5, -w3d2],
    [-0.5, -w3d2],
    [-1, 0],
    [-0.5, w3d2]
    ]

    for punkt in eckpunkte:
        liste = np.array([sPx + punkt[0], sPy + punkt[1], 0]).reshape(1, 3)
        corners = np.vstack((corners, liste))


def add_lines(anzahl_Sechsecke):
    global linien  
    linie_start = 1
    for i in range(anzahl_Sechsecke):
        for j in range(5):
            neue_linie = [linie_start, linie_start + 1]
            neuer_array = np.array(neue_linie).reshape(1, 2)
            if linien.size == 0:
                linien = neuer_array
            else:
                linien = np.append(linien, neuer_array, axis=0)
            linie_start += 1
        neue_linie = [linie_start, linie_start - 5]
        neuer_array = np.array(neue_linie).reshape(1, 2)
        linien = np.append(linien, neuer_array, axis=0)
        linie_start += 1


### Programm ###
os.system('clear')
while True:
    try:
        namecsv = input('''
Name von Datei für Visualisierung eingeben (nur Name, ohne Endung und Pfad): 
''')
        with open('Experimente/ProgrammPandasO3d/CSV/' + namecsv + '.csv', 'r'):  # Versucht Datei zu öffnen
            break  
    
    except FileNotFoundError:
        os.system('clear')
        print('Keine Datei mit diesem Namen gefunden.')


start = time.time()
dateicsv = 'Experimente/ProgrammPandasO3d/CSV/' + namecsv + '.csv'


with open(dateicsv, "r") as csvDatei:
    csvLesen = csv.reader(csvDatei)
    for zeile in csvLesen:
        anzahl_zeilen += 1
        xHex, yHex = 0, 0
        yHex = int(zeile[0]) * np.sqrt(3)
        if int(zeile[1]) % 2 == 0:
            yHex -= w3d2
        xHex = int(zeile[1]) * 1.5
        newCorners(xHex, yHex)


add_lines(anzahl_zeilen*6)

hexagon = o3d.geometry.LineSet(
    points=o3d.utility.Vector3dVector(corners),
    lines=o3d.utility.Vector2iVector(linien))

hexagons = [hexagon]
zeit = time.time()-start
o3d.visualization.draw_geometries(hexagons)
os.system('clear')
print(namecsv, 
''' 

Anzahl Zellen:      ''', anzahl_zeilen, 
'''
Berechnungszeit:    ''', round(zeit, 3) , 's')
print(corners)