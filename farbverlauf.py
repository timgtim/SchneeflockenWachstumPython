#Farbverlauf für mpl Visualisierung, je nach Zellwert anderen Farbe
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import RegularPolygon
import numpy as np


z_liste = [0.2, 0.5, 0.8, 0.99]


colors = ['#b4e2fa', '#0c425e'] #hellblau bis dunkelblau
cmap = mcolors.LinearSegmentedColormap.from_list('Blau', colors, N=100)

x_liste = [0.2, 0.4, 0.6, 0.8]  
y_liste = [0.5, 0.5, 0.5, 0.5]  


fig, ax = plt.subplots()
for x, y, z in zip(x_liste, y_liste, z_liste):
    #farbe aus cmap
    farbe = cmap(z)
    

    hex = RegularPolygon((x, y), numVertices=6, radius=0.1, alpha=1, edgecolor='k', facecolor=farbe)
    ax.add_patch(hex)

plt.show()
