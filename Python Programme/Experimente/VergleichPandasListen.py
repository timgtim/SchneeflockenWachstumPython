#Verleich der Rechengeschwindigketen und Dateigrössen von Listen und Pandas

import numpy as np
import pandas as pd
from sys import getsizeof
import time

wert = 20
spalten =   100
zeilen =    100
länge = spalten*zeilen
anzahl_durchgänge = 1000
counter = 0

tabelle1 = pd.DataFrame(wert, index=range(spalten), columns=range(zeilen))
liste = [wert for i in range(länge)]
np_array = np.array((liste), dtype=np.float64)

def grössen(array, liste, tabelle):
    print('Np Array:    ', getsizeof(array))
    print('Liste:       ', getsizeof(liste))
    print('Tabelle:     ', getsizeof(tabelle))


def rechnung_Array(array):
    for i in range(anzahl_durchgänge):
        for i in range(zeilen*spalten):
            array[i] = array[i]*2/54
    return array

def rechnung_List(list):
    for i in range(anzahl_durchgänge):
        for i in range(zeilen*spalten):
            list[i] = list[i]*2/54
    return list

def rechnung_Tabelle(tabelle):
    for i in range(anzahl_durchgänge):
        for i in range(zeilen-1):
            for y in range(spalten-1):
                tabelle.at[i, y] = tabelle.at[i, y]*2/54
    return tabelle

print('Dateigrössen: ')
grössen(np_array, liste, tabelle1)
print('\n================================================================')


start = time.time()
rechnung_Array(np_array)
print('\nBerechnungszeit Np Arrays:  ', time.time()-start)

start = time.time()
rechnung_List(liste)
print('Berechnungszeit Liste:           ', time.time() - start)

start = time.time()
rechnung_Tabelle(tabelle1)
print('Berechnungszeit Pandas:          ', time.time() - start)




