from multiprocessing import Pool
import time

n = 6
ursprungsliste = [i for i in range(500000)]
schlussliste = []
index = []


#Länge jeder Teilliste berechnen
listenteil = len(ursprungsliste) // n
rest = len(ursprungsliste) % n

#Ursprungsliste unterteilen
for i in range(n):
    if len(index) == 0:
        startIndex = 0
        endIndex = listenteil
    else:
        startIndex = endIndex
        endIndex = startIndex + listenteil
    index.append((startIndex, endIndex))

def meine_funktion(start, end):
    global ursprungsliste
    for i in range(start, end):
        ursprungsliste[i] = ursprungsliste[i] ** 2 ** 3 ** 2
    return ursprungsliste[start:end]

if __name__ == "__main__":
    start = time.time()
    pool = Pool(processes=6)  # Prozessorkerne angeben
    ergebnisse = pool.starmap(meine_funktion, index)
    pool.close()
    pool.join()
    for teil in ergebnisse:
        schlussliste.extend(teil)  #Teilliste zu schlussliste hinzufügen
    print(schlussliste[0:10])
    print(f'\nMulticoreprocessing Zeit: {time.time()-start} s')

    start = time.time()
    for i in range(len(ursprungsliste)):
        ursprungsliste[i] = ursprungsliste[i]**2**3**2
    print(ursprungsliste[0:10])
    print(f'\nSingleprocessing Zeit: {time.time()-start}s')