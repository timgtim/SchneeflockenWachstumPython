#Test für Performance bei vielen gezeichneten Linien

import open3d as o3d
import numpy as np
import os
import random
import time

n = 36000
degrees = 0
rd = 1

def zeitStart():
    global startZeit
    startZeit = time.time()


def zeitStop():
    stopZeit = time.time()
    print('''

----------------------------------------
Zeit: ''', round((stopZeit - startZeit), 3),  ''' s
----------------------------------------

''')


def newCorners():
    global corners, n, degrees, rd
    for i in range(n):
        liste = [np.cos(degrees), np.sin(degrees), 0]
        new_array = np.array(liste).reshape(1, 3)
        corners = np.append(corners, new_array, axis=0)
        degrees += 0.01

def newLines():
    for i in range(n):
        global lines
        liste = [random.randint(0, n), random.randint(0, n)]
        new_array = np.array(liste).reshape(1, 2)
        lines = np.append(lines, new_array, axis=0)
    

corners = np.array([   
   [0, 0, 0],
   [0, 0, 1]
])


lines = np.array([    
    [1, 0]
])

zeitStart()
newCorners()
newLines()


hexagon = o3d.geometry.LineSet(
    points=o3d.utility.Vector3dVector(corners),
    lines=o3d.utility.Vector2iVector(lines)
)


hexagons = [hexagon]


time.sleep(4)

os.system('clear')
print('''Corners: 
''', corners)
print('''
Hexagons: ''', hexagons)
print('''


''')
zeitStop()
o3d.visualization.draw_geometries(hexagons)
