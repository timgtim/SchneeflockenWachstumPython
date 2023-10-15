import csv, math, time, os

def durchschnitt(index, zeilen,  länge_Liste, beta, l_Zellen): #Durchschnitt der 6 Nachbarzellen von Zelle index Berechnen
    if index%zeilen%2 != 0: #gerade Spalten

        if index >= zeilen: #oben
            feld1 = l_Zellen[index - zeilen]
            if feld1 >= 1 or rezeptiv(index - zeilen, zeilen, länge_Liste, l_Zellen):
                feld1 = 0
        else:
            feld1 = beta

        if (index-zeilen+1) % zeilen != 0: #Rechts
            feld2 = l_Zellen[index + 1]
            if feld2 >= 1 or rezeptiv(index + 1, zeilen, länge_Liste, l_Zellen):
                feld2 = 0
        else: 
            feld2 = beta

        if  index < länge_Liste-zeilen and (index-zeilen+1)%zeilen != 0: #UntenRechts 
            feld3 = l_Zellen[index + zeilen + 1]
            if feld3 >= 1 or rezeptiv(index + zeilen + 1, zeilen, länge_Liste, l_Zellen):
                feld3 = 0
        else:
            feld3 = beta
        
        if index < länge_Liste-zeilen: #Unten
            feld4 = l_Zellen[index + zeilen]
            if feld4 >= 1 or rezeptiv(index + zeilen, zeilen, länge_Liste, l_Zellen):
                feld4 = 0
        else:
            feld4 = beta
        
        if index < länge_Liste-zeilen and (index+zeilen+1)%zeilen != 0: #UntenLinks
            feld5 = l_Zellen[index + zeilen - 1]
            if feld5 >= 1 or rezeptiv(index + zeilen - 1, zeilen, länge_Liste, l_Zellen):
                feld5 = 0
        else:
            feld5 = beta
        
        if index%zeilen != 0: #Links
            feld6 = l_Zellen[index - 1]
            if feld6 >= 1 or rezeptiv(index - 1, zeilen, länge_Liste, l_Zellen):
                feld6 = 0
        else:
            feld6 = beta


    else:
        if index >= zeilen: #Oben
            feld1 = l_Zellen[index - zeilen] 
            if feld1 >= 1 or rezeptiv(index - zeilen, zeilen, länge_Liste, l_Zellen):
                feld1 = 0
        else:
            feld1 = beta

        if index >= zeilen and (index-zeilen+1)%zeilen != 0: #ObenRechts
            feld2 = l_Zellen[index - zeilen + 1]
            if feld2 >= 1 or rezeptiv(index - zeilen + 1, zeilen, länge_Liste, l_Zellen):
                feld2 = 0
        else:
            feld2 = beta
        
        if (index-zeilen+1) % zeilen != 0: #Rechts
            feld3 = l_Zellen[index + 1]
            if feld3 >= 1 or rezeptiv(index + 1, zeilen, länge_Liste, l_Zellen):
                feld3 = 0
        else:
            feld3 = beta
        
        if index < länge_Liste-zeilen: #Unten
            feld4 = l_Zellen[index + zeilen]
            if feld4 >= 1 or rezeptiv(index + zeilen, zeilen, länge_Liste, l_Zellen):
                feld4 = 0
        else:
            feld4 = beta

        if index%zeilen != 0: #Links
            feld5 = l_Zellen[index - 1]
            if feld5 >= 1 or rezeptiv(index - 1, zeilen, länge_Liste, l_Zellen):
                feld5 = 0
        else:
            feld5 = beta

        if index >= zeilen and index%zeilen != 0: #Obenlinks
            feld6 = l_Zellen[index - zeilen - 1]
            if feld6 >= 1 or rezeptiv(index - zeilen - 1, zeilen, länge_Liste, l_Zellen):
                feld6 = 0
        else:
            feld6 = beta

    durchschnittNachbarn = (feld1 + feld2 + feld3 + feld4 + feld5 + feld6)/6
    return durchschnittNachbarn

def rezeptiv(index, zeilen, länge_Liste, l_Zellen): #überprüfen, ob Zelle index rezeptiv ist, weil sie eine gefrorene Nachbarzelle hat

    if index%zeilen%2 != 0: #gerade Spalten (weil Index bei 0 beginnt um 1 verschoben)
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



def main(zeilen, alpha, beta, gamma):
    global l_AktZellen, l_Zellen

    pfad = 'ProgrammReitersModell/Dateien/csvDateien/' #Hier wird CSV-Datei gespeichert
    dateiname = f'Z{zeilen}A{alpha}B{beta}G{gamma}.csv'
    counter = 0
    anzahl_Zellen = 0
    loopW = True   
    kern = 1  
    spalten = zeilen
    länge_Liste =   zeilen*spalten
    kern_Position = int(zeilen/2)*zeilen+int(zeilen/2) #Mittelpunkt von Simulationsanordnung, bei keinem klaren Mittelpunkt auf unterer, rechter Seite
    l_Zellen = [beta for i in range(länge_Liste)]
    l_AktZellen = l_Zellen
    l_Zellen[kern_Position] = kern
    l_AktZellen = l_Zellen.copy()
    start = time.time()

    while loopW:
        print('Duchgangsnummer: ', counter)
    
        for i in range(länge_Liste): #Aktualisierungsdurchgänge, bei jeder Zelle werden Aktualisierungsfunktionen durchgeführt
            diffusionswert = l_Zellen[i]

            if diffusionswert >= 1 or rezeptiv(i, zeilen, länge_Liste, l_Zellen): #Diffusion
                diffusionswert = 0
            diffusion = (alpha/2)*(durchschnitt(i, zeilen, länge_Liste, beta, l_Zellen )-diffusionswert)
            l_AktZellen[i] += diffusion


            if diffusionswert == 0: #Konstante Addition
                l_AktZellen[i] += gamma

        l_Zellen = l_AktZellen.copy() #Aktualisierte Zellwerte in Ursprungsliste kopieren
        counter += 1

        for i in l_Zellen[(zeilen-3)*zeilen:]: #Überprüfen, ob Schneeflocke Rand von Simulation erreicht hat
            if i >= 1:
                loopW = False


    zeit = round(time.time() - start, 3)

    
    name = pfad + dateiname
    ersteZeile = ['Alpha', alpha, 'Beta', beta, 'Gamma', gamma, 'Zeilen', zeilen] #Informationen zu Schneeflocke wird in erste Zeile von CSV Datei geschrieben
                    
    with open(name, 'a', encoding='utf-8') as csv_schreib_datei:
        writer = csv.writer(csv_schreib_datei)
        writer.writerow(ersteZeile)  

    for i in range(länge_Liste): 
        if l_Zellen[i] >= 1: #die Koordinaten von jeder gefrorenen Zelle werden in die CSV-Datei geschrieben
            anzahl_Zellen += 1
            x = math.ceil(i/zeilen) #aus Index den Zeilenwert berechnen
            y = i%zeilen #aus Index den Spaltenwert berechnen
            z = l_Zellen[i] #Zellwert von Zelle i
            liste_xyz = [x, y, z]
                    
            with open(name, 'a', encoding='utf-8') as csv_schreib_datei:
                writer = csv.writer(csv_schreib_datei)
                writer.writerow(liste_xyz)  


    os.system('clear')
    print(f'''
Datei [{dateiname}] erstellt!

Berechnungszeit für {counter} Aktualisierungsdurchgänge: {zeit} Sekunden
          
Schneeflocke mit {anzahl_Zellen} Zellen erstellt.
Alpha: {alpha}
Beta: {beta}
Gamma: {gamma}''')
    
    return dateiname



def mainFürGif(zeilen, alpha, beta, gamma, gifAbstand=5):
    global l_AktZellen, l_Zellen
    
    counter = 0
    loopW = True   
    dateizähler = 1
    anzahl_Zellen = 0
    kern = 1
    if zeilen%2 != 0:
        zeilen += 1  
    spalten = zeilen
    länge_Liste =   zeilen*spalten
    kern_Position = int(länge_Liste/2)+int(zeilen/2)-1     
    l_Zellen = [beta for i in range(länge_Liste)]
    l_AktZellen = l_Zellen
    l_Zellen[kern_Position] = kern
    l_AktZellen = l_Zellen.copy()
    start = time.time()
    gifAbstandDynamisch = gifAbstand

    ordner = str(f'ProgrammReitersModell/Dateien/Animationen/Z{zeilen}A{alpha}B{beta}G{gamma}')
    if not os.path.exists(ordner):
        os.makedirs(ordner)

    ordnerGif = str(f'ProgrammReitersModell/Dateien/Animationen/Z{zeilen}A{alpha}B{beta}G{gamma}/GifOrdner')
    if not os.path.exists(ordnerGif):
        os.makedirs(ordnerGif)
    

    while loopW:
        print('Duchgangsnummer: ', counter)
    
        for i in range(länge_Liste):
            diffusionswert = l_Zellen[i]

            if diffusionswert >= 1 or rezeptiv(i, zeilen, länge_Liste, l_Zellen):
                diffusionswert = 0
            diffusion = (alpha/2)*(durchschnitt(i, zeilen, länge_Liste, beta, l_Zellen )-diffusionswert)
            l_AktZellen[i] += diffusion

            if diffusionswert == 0:
                l_AktZellen[i] += gamma

        l_Zellen = l_AktZellen.copy()
        counter += 1

        for i in l_Zellen[(zeilen-3)*zeilen:]: #Überprüfen, ob Schneeflocke Rand von Simulation erreicht hat
            if i >= 1:
                loopW = False
        if 0 <= kern_Position + gifAbstandDynamisch < len(l_Zellen) and l_Zellen[kern_Position + gifAbstandDynamisch] >= 1: #Wenn Arm von Schneeflocke eine festgelegte Zellanzahl gewachsen ist, wird eine csv datei erstellt
            if l_Zellen[kern_Position + gifAbstandDynamisch] >= 1 and (kern_Position + gifAbstandDynamisch)<(länge_Liste-1):
                gifAbstandDynamisch += gifAbstand
                name = 'gif' + str(dateizähler) #Dateinamen werden nummeriert
                dateizähler += 1
                dateiname = ordnerGif + '/' + str(name) + '.csv'
                ersteZeile = ['Alpha', alpha, 'Beta', beta, 'Gamma', gamma, 'Zeilen', zeilen]
                        
        
                with open(dateiname, 'a', encoding='utf-8') as csv_schreib_datei:
                    writer = csv.writer(csv_schreib_datei)
                    writer.writerow(ersteZeile)  

                for i in range(länge_Liste):
                    if l_Zellen[i] >= 1:
                        x = math.ceil(i/zeilen)
                        y = i%zeilen
                        z = l_Zellen[i]
                        listexy = [x, y, z]
                                
                        with open(dateiname, 'a', encoding='utf-8') as csv_schreib_datei:
                            writer = csv.writer(csv_schreib_datei)
                            writer.writerow(listexy)  

    ersteZeile = ['Alpha', alpha, 'Beta', beta, 'Gamma', gamma, 'Zeilen', zeilen]

    name = 'gif' + str(dateizähler)
    dateiname = ordnerGif + '/' + str(name) + '.csv'
    with open(dateiname, 'a', encoding='utf-8') as csv_schreib_datei:
        writer = csv.writer(csv_schreib_datei)
        writer.writerow(ersteZeile)  
    for i in range(länge_Liste):
        if l_Zellen[i] >= 1:
            x = math.ceil(i/zeilen)
            y = i%zeilen
            z = l_Zellen[i]
            liste_xyz = [x, y, z]
                    
            with open(dateiname, 'a', encoding='utf-8') as csv_schreib_datei:
                writer = csv.writer(csv_schreib_datei)
                writer.writerow(liste_xyz) 


    zeit = round(time.time() - start, 3)
    pfad = 'ProgrammReitersModell/Dateien/csvDateien/'
    dateiname = f'Z{zeilen}A{alpha}B{beta}G{gamma}.csv'
    name = pfad + dateiname
    
   
                    
    with open(name, 'a', encoding='utf-8') as csv_schreib_datei:
        writer = csv.writer(csv_schreib_datei)
        writer.writerow(ersteZeile)  

    for i in range(len(l_Zellen)):
        if l_Zellen[i] >= 1:
            anzahl_Zellen += 1
            x = math.ceil(i/zeilen)
            y = i%zeilen
            z = l_Zellen[i]
            liste_xyz = [x, y, z]
                    
            with open(name, 'a', encoding='utf-8') as csv_schreib_datei:
                writer = csv.writer(csv_schreib_datei)
                writer.writerow(liste_xyz)  

    print(f'''
Datei [{dateiname}] erstellt!

Berechnungszeit für {counter} Aktualisierungsdurchgänge: {zeit} Sekunden
          
Schneeflocke mit {anzahl_Zellen} Zellen erstellt.
Alpha: {alpha}
Beta: {beta}
Gamma: {gamma}

Anzahl Dateien für Gif: {dateizähler}''')
    return ordnerGif




if __name__ == '__main__':
    q = 1