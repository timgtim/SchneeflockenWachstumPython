import matplotlib.pyplot as plt
import time, os

counter = 1
circle_radius = 0.5

os.system('clear')
while True:
    try:
        namecsv = input('''
Name von Datei für Visualisierung (nur Name, ohne Endung und Pfad): 
''')
        namecsv = 'Experimente/' + namecsv + '.csv'       
        with open(namecsv, 'r'):  # Versucht Datei zu öffnen
            break  
    
    except FileNotFoundError:
        os.system('clear')
        print('Keine Datei mit diesem Namen gefunden.')

start = time.time()
x_liste = []
y_liste = []

# Daten aus der CSV-Datei lesen
with open(namecsv, 'r') as file:
    lines = file.readlines()
    for line in lines:  
        x, y, z = line.strip().split(',')
        x = float(x) 
        y = float(y)
        if y%2 != 0: #Koordinaten richtig anordnen, versetzte Spalten
            x = x + 0.5
        y = y * 3**0.5/2
   
        x_liste.append(float(x))
        y_liste.append(float(y))
        
            
csv_zeit = time.time() - start
start = time.time()
plt.figure()

#Kreise an Koordinaten zeichnen
for x, y in zip(x_liste, y_liste):
    circle = plt.Circle((x, y), radius=circle_radius, color='black', fill=False)
    plt.gca().add_patch(circle)

plt.xlabel('X-Koordinate')
plt.ylabel('Y-Koordinate')
plt.title('Schneeflocke')

#plt.savefig("High resoltion.png",dpi=800) 


plt.axis('equal')  #Achsen gleich skaliert
grafik_zeit = time.time() - start
plt.show()

os.system('clear')
print(namecsv, 
''' 

Anzahl Zellen:      ''', len(lines), 
'''
Zeit Auslesen csv Datei:    ''', round(csv_zeit, 3) , 's', 
'''
Zeit Visualisierung:    ''', round(grafik_zeit, 3) , 's')
