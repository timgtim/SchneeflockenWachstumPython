import csv
import random

dateiname = 'Experimente/Koordinaten.csv'
punkte = 10000
koordinaten = []


for _ in range(punkte):
    x = random.randint(0, 1000)  
    y = random.randint(0, 1000)  
    koordinaten.append((x, y))

with open(dateiname, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(koordinaten)

