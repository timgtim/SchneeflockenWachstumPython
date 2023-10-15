'''
Liste aufteilen: Länge Liste / prozessorkerne, oben und unten eine zeile dazufügen, damit es keine Konflikte mit unterer/oberer Zeile gibt
nur liste ohne oberen und unteren teil iterieren, am schluss ohne zwsischenteil zusammensetzen
'''
'''
Zeit hat nicht gereicht um das Programm fertig zu schreiben, so dass es funktioniert
'''
import csv, math, time
from multiprocessing import Pool

#Variabeln
zeilen =        10 + 2
spalten =       zeilen          
alpha =         1        
beta =          0.9
gamma =         0.1
counter =       0
kern =          1  
loopW =         True    
länge_Liste =   zeilen*spalten
kern_Position = int(länge_Liste/2)+int(zeilen/2)-1 

l_Zellen = [beta for i in range(länge_Liste)]
l_AktZellen = l_Zellen

prozessorkerne = 6
index = []



def durchschnitt(index):
    if index%2 != 0: #gerade Spalten
        global feld1, feld2, feld3, feld4, feld5, feld6, zeilen, l_Zellen
        
        if index >= zeilen: #oben
            feld1 = l_Zellen[index - zeilen]
            if feld1 >= 1 or rezeptiv(index - zeilen):
                feld1 = 0
        else:
            feld1 = beta

        if (index-zeilen+1) % zeilen != 0: #Rechts
            feld2 = l_Zellen[index + 1]
            if feld2 >= 1 or rezeptiv(index + 1):
                feld2 = 0
        else: 
            feld2 = beta

        if  index < länge_Liste-zeilen and (index-zeilen+1)%zeilen != 0: #UntenRechts 
            feld3 = l_Zellen[index + zeilen + 1]
            if feld3 >= 1 or rezeptiv(index + zeilen + 1):
                feld3 = 0
        else:
            feld3 = beta
        
        if index < länge_Liste-zeilen: #Unten
            feld4 = l_Zellen[index + zeilen]
            if feld4 >= 1 or rezeptiv(index + zeilen):
                feld4 = 0
        else:
            feld4 = beta
        
        if index < länge_Liste-zeilen and (index+zeilen+1)%zeilen != 0: #UntenLinks
            feld5 = l_Zellen[index + zeilen - 1]
            if feld5 >= 1 or rezeptiv(index + zeilen - 1):
                feld5 = 0
        else:
            feld5 = beta
        
        if index%zeilen != 0: #Links
            feld6 = l_Zellen[index - 1]
            if feld6 >= 1 or rezeptiv(index - 1):
                feld6 = 0
        else:
            feld6 = beta


    else:
        if index >= zeilen: #Oben
            feld1 = l_Zellen[index - zeilen] 
            if feld1 >= 1 or rezeptiv(index - zeilen):
                feld1 = 0
        else:
            feld1 = beta

        if index >= zeilen and (index-zeilen+1)%zeilen != 0: #ObenRechts
            feld2 = l_Zellen[index - zeilen + 1]
            if feld2 >= 1 or rezeptiv(index - zeilen + 1):
                feld2 = 0
        else:
            feld2 = beta
        
        if (index-zeilen+1) % zeilen != 0: #Rechts
            feld3 = l_Zellen[index + 1]
            if feld3 >= 1 or rezeptiv(index + 1):
                feld3 = 0
        else:
            feld3 = beta
        
        if index < länge_Liste-zeilen: #Unten
            feld4 = l_Zellen[index + zeilen]
            if feld4 >= 1 or rezeptiv(index + zeilen):
                feld4 = 0
        else:
            feld4 = beta

        if index%zeilen != 0: #Links
            feld5 = l_Zellen[index - 1]
            if feld5 >= 1 or rezeptiv(index - 1):
                feld5 = 0
        else:
            feld5 = beta

        if index >= zeilen and index%zeilen != 0: #Obenlinks
            feld6 = l_Zellen[index - zeilen - 1]
            if feld6 >= 1 or rezeptiv(index - zeilen - 1):
                feld6 = 0
        else:
            feld6 = beta

    durchschnittNachbarn = (feld1 + feld2 + feld3 + feld4 + feld5 + feld6)/6
    return durchschnittNachbarn

def rezeptiv(index):
    global l_Zellen
    if index%2 != 0: #gerade Spalten (weil Index bei 0 beginnt um 1 verschoben)
        if index >= zeilen: #Oben
            if  l_Zellen[index - zeilen] >= 1:
                return True
      
        if (index-zeilen+1) % zeilen != 0: #Rechts
            if l_Zellen[index + 1] >= 1:
                return True
      
        if  index < länge_Liste-zeilen and (index-zeilen+1)%zeilen != 0: #UntenRechts 
            if l_Zellen[index + zeilen + 1 ] >= 1:
                return True
     
        if index < länge_Liste-zeilen: #Unten
            if l_Zellen[index + zeilen] >= 1:
                return True
        
        if index < länge_Liste-zeilen and (index+zeilen+1)%zeilen != 0: #UntenLinks
            if l_Zellen[index + zeilen - 1] >= 1:
                return True
       
        if index%zeilen != 0: #Links
            if l_Zellen[index - 1] >= 1:
                return True
        return False
        
    else:

        if index >= zeilen: #Oben
            if l_Zellen[index - zeilen] >= 1:
                return True

        if index >= zeilen and (index-zeilen+1)%zeilen != 0: #ObenRechts
            if l_Zellen[index - zeilen + 1] >= 1:
                return True
     

        if (index-zeilen+1) % zeilen != 0: #Rechts
            if l_Zellen[index + 1 ] >= 1:
                return True
    
        if index < länge_Liste-zeilen: #Unten
            if l_Zellen[index + zeilen] >= 1:
                return True
      
        if index%zeilen != 0: #Links
            if l_Zellen[index - 1] >= 1:
                return True
       
        if index >= zeilen and index%zeilen != 0: #Obenlinks
            if l_Zellen[index - zeilen - 1] >= 1:
                return True   
        return False


####Simulation################################################################################################

l_Zellen[kern_Position] = kern
l_AktZellen = l_Zellen.copy()
start = time.time()

# Berechne die Länge jeder Teilliste
listenteil = len(l_Zellen) // prozessorkerne
rest = len(l_Zellen) % prozessorkerne

# Ursprungsliste unterteilen
for i in range(prozessorkerne):
    if len(index) == 0:
        startIndex = 0
        endIndex = listenteil
    else:
        startIndex = endIndex
        endIndex = startIndex + listenteil
    index.append((startIndex, endIndex))

def multiprocessing_Simulation(start, end):
    global l_Zellen, l_AktZellen, zeilen
    startAnpassen = zeilen
    endAnpassen = zeilen
    if start == 0:
        startAnpassen = 0
    if end == zeilen:
        endAnpassen = 0
    
    for i in range(start + startAnpassen, end-endAnpassen):
        diffusionswert = l_Zellen[i]

        if diffusionswert >= 1 or rezeptiv(i):
            diffusionswert = 0
        
        diffusion = (alpha/2)*(durchschnitt(i)-diffusionswert)
        l_AktZellen[i] += diffusion

        if diffusionswert == 0:
            l_AktZellen[i] += gamma




if __name__ == '__main__':
    while loopW:
        print('Duchgangsnummer: ', counter)
     
        pool = Pool(processes=prozessorkerne)
        berechnen = pool.starmap(multiprocessing_Simulation, index)
        pool.close()
        pool.join()

        l_Zellen = l_AktZellen.copy()
        counter += 1

        for i in range(3*zeilen):
            if l_Zellen[i] >= 1:
                loopW = False

        


    zeit = time.time() - start
    print('l_Zellen', l_Zellen)

    print('l_AktZellen', l_AktZellen)
    name = input('Dateiname: ')
    if name != 'nichts':
        dateiname = 'csv/' + str(name) + '.csv'
        for i in range(länge_Liste):
            if l_Zellen[i] >= 1:
                x = math.ceil(i/zeilen)
                y = i%zeilen
                listexy = [x, y]
                        
                with open(dateiname, 'a', encoding='utf-8') as csv_schreib_datei:
                    writer = csv.writer(csv_schreib_datei)
                    writer.writerow(listexy)  

    print('Datei:', name, 'erstellt.')
    print('Berechnungszeit: ', zeit)