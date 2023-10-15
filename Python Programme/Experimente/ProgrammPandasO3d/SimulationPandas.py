import pandas as pd, os, csv, time


#Variabeln
zeilen = 250     #evtl. ungerade, damit Eiskern in Mitte ist
spalten = zeilen    #evtl. ungerade, damit Eiskern in Mitte ist
alpha = 1    #Konstante in Diffusionsgleichung
beta = 0.4   #Konstante für Hintergrundfeuchtigkeit
gamma = 0.01  #Konstanter Wert für Addition bei rezeptiven Zelle
kern = 1        #Wert von Eiskern in der Mitte


inzeile1, inletzterzeile, inspalte1, inletzerspalte = False, False, False, False #Für Abbruch von Aktualisierung, wenn eine Rezeptive Zelle den Rand erreicht
counter = 0
abbruchloop = 3 #wenn Zellwert über 1 in dieser Zeile/Spalte -> Aktualisierung fertig


###Funktionen###
#Durchschnitt der 6 Nachbarszelle
def durchschnitt(zeile, spalte):

    if spalte%2 == 0 : #Form T, ungerade Zahl, wegen Randzelle ist %2 == 0 ungerade
    # Feld1        
        try: 
            feld1 = tabelle.at[zeile-1, spalte]
            if feld1 >= 1 or nachbarRezeptiv(zeile-1, spalte): #Wenn zelle Rezeptiv, kein Wasser in Zelle beteiligt sich an Diffusion
                feld1 = 0
        except Exception as e:
            print('Fehler in gerader Zelle, Feld 1', e)
            feld1 = beta
        
    #Feld2
        try:
            feld2 = tabelle.at[zeile-1, spalte + 1]
            if feld2 >= 1 or nachbarRezeptiv(zeile-1, spalte+1):
                feld2 = 0
        except:
            print('Fehler in gerader Zelle, Feld 2')
            feld2 = beta

    #Feld3
        try:
            feld3 = tabelle.at[zeile, spalte+1]      
            if feld3 >= 1 or nachbarRezeptiv(zeile, spalte+1):
                feld3 = 0 
        except:
            print('Fehler in gerader Zelle, Feld 3')
            feld3 = beta

    #Feld4
        try:
            feld4 = tabelle.at[zeile+1, spalte]
            if feld4 >= 1 or nachbarRezeptiv(zeile+1, spalte):
                feld4 = 0
        except:
            print('Fehler in gerader Zelle, Feld 4')
            feld4  = beta

    #Feld5
        try:
            feld5 = tabelle.at[zeile, spalte-1]
            if feld5 >= 1 or nachbarRezeptiv(zeile, spalte-1):
                feld5 = 0
        except:
            print('Fehler in gerader Zelle, Feld 5')
            feld5 = beta

    #Feld6
        try:
            feld6 = tabelle.at[zeile-1, spalte-1]
            if feld6 >= 1 or nachbarRezeptiv(zeile-1, spalte-1):
                feld6 = 0
        except:
            print('Fehler in gerader Zelle, Feld 6')
            feld6 = beta
    

            
        durchschnitt = (feld1 + feld2 + feld3 + feld4 + feld5 + feld6)/6
            
        return durchschnitt



            
        #except:
           # print('Fehler in Durchschnitt, gerade (Form T)')
          ##  return beta


    else: #Form umgekehrtes T
    # Feld1        
        try: 
            feld1 = tabelle.at[zeile-1, spalte]
            if feld1 >= 1 or nachbarRezeptiv(zeile-1, spalte): #Wenn zelle Rezeptiv, kein Wasser in Zelle beteiligt sich an Diffusion
                feld1 = 0
        except Exception as e:
            print('Fehler in ungerader Zelle, Feld 1', 'Fehler: ', e, 'Zeile: ', zeile, 'Spalte: ', spalte)
            feld1 = beta
        
    #Feld2
        try:
            feld2 = tabelle.at[zeile, spalte + 1]
            if feld2 >= 1 or nachbarRezeptiv(zeile, spalte+1):
                feld2 = 0
        except:
            print('Fehler in ungerader Zelle, Feld 2')
            feld2 = beta

    #Feld3
        try:
            feld3 = tabelle.at[zeile+1, spalte+1]      
            if feld3 >= 1 or nachbarRezeptiv(zeile+1, spalte+1):
                feld3 = 0 
        except:
            print('Fehler in ungerader Zelle, Feld 3')
            feld3 = beta

    #Feld4
        try:
            feld4 = tabelle.at[zeile+1, spalte]
            if feld4 >= 1 or nachbarRezeptiv(zeile+1, spalte):
                feld4 = 0
        except:
            print('Fehler in ungerader Zelle, Feld 4')
            feld4 = beta

    #Feld5
        try:
            feld5 = tabelle.at[zeile+1, spalte-1]
            if feld5 >= 1 or nachbarRezeptiv(zeile+1, spalte-1):
                feld5 = 0
        except:
            print('Fehler in ungerader Zelle, Feld 5')
            feld5 = beta

    #Feld6
        try:
            feld6 = tabelle.at[zeile, spalte-1]
            if feld6 >= 1 or nachbarRezeptiv(zeile, spalte-1):
                feld6 = 0
        except:
            print('Fehler in gerader Zelle, Feld 6')
            feld6 = beta

            
        durchschnitt = (feld1 + feld2 + feld3 + feld4 + feld5 + feld6)/6
            
        return durchschnitt

#Prüfen ob rezeptiv
def nachbarRezeptiv(zeile, spalte):
    if spalte%2 == 0 : #Form T, ungerade Zahl
        #try:   
        if tabelle.at[zeile-1, spalte] >= 1 or tabelle.at[zeile-1, spalte + 1] >= 1 or tabelle.at[zeile, spalte+1] >= 1 or tabelle.at[zeile+1, spalte] >= 1 or tabelle.at[zeile, spalte-1] >= 1 or tabelle.at[zeile-1, spalte-1] >= 1:
            return True
        else:
            return False
        #except:
          #  print('Fehler in nachbarRezeptiv , gerade (Form T)')



    else: #Form umgekehrtes T
        #try:  
        if tabelle.at[zeile-1, spalte] >= 1 or tabelle.at[zeile, spalte + 1] >= 1 or tabelle.at[zeile+1, spalte+1] >= 1 or tabelle.at[zeile+1, spalte] >= 1 or tabelle.at[zeile+1, spalte-1] >= 1 or tabelle.at[zeile, spalte-1] >= 1:
            return True
        else:
            return False
    
        #except:
           # print('Fehler in nachbarRezeptiv, ungerade (Form umgekehrtes T)')


#################################

start = time.time()

#Tabelle mit Hintergrundfeuchtigkeit beta füllen
tabelle = pd.DataFrame(beta, index=range(zeilen+2), columns=range(spalten+2))
aktualisierungsTabelle = pd.DataFrame(beta, index=range(zeilen+2), columns=range(spalten+2))

#Eiskern in Mitte von Tabelle
x, y= int(zeilen/2), int(spalten/2)
tabelle.at[x, y] = kern
aktualisierungsTabelle.at[x, y] = kern

#Simulation Daten

print(tabelle)
while True:
    counter += 1
    for zeilezelle in range(2, zeilen-1): #erst bei zweiter Zeile anfangen wegen Betazeile, erste und letzte Zeile auslassen, sollte eigentlich range(1, zeilen-0) sein
        for spaltezelle in range(2, spalten-1): 

            #Diffusion
            diffusionswert = tabelle.at[zeilezelle, spaltezelle]

            if diffusionswert >= 1 or nachbarRezeptiv(zeilezelle, spaltezelle) == True:
                diffusionswert = 0
            diffusion = (alpha/2) * (durchschnitt(zeilezelle, spaltezelle) - diffusionswert)
            aktualisierungsTabelle.at[zeilezelle, spaltezelle] += diffusion
                

            #Addition rezeptive Zellen
            if tabelle.at[zeilezelle, spaltezelle] >= 1 or nachbarRezeptiv(zeilezelle, spaltezelle):
                aktualisierungsTabelle.at[zeilezelle, spaltezelle] += gamma


    tabelle = aktualisierungsTabelle.copy() #Nach Aktualisierung von allen Zellen die normale 

    inzeile1 = (tabelle.loc[abbruchloop] >= 1).any()
    inletzterzeile = (tabelle.loc[zeilen-abbruchloop]>= 1).any()
    inspalte1 = (tabelle[abbruchloop] >= 1).any()
    inletzterspalte = (tabelle[spalten-abbruchloop] >= 1).any()

    if inzeile1 or inletzterzeile or inspalte1 or inletzterspalte:
        break
   
    os.system('clear')
    print('''
Durchgang Nr. ''' , str(counter))
    print()
    
    
zeit = time.time() - start

#Daten für Visualisierung in csv schreiben
name = input('Dateiname: ')
dateiname = 'Experimente/ProgrammPandasO3d/CSV/'+ str(name) + '.csv'
for zeilezelle in range(zeilen):
    print(tabelle)
    for spaltezelle in range(spalten):
        if tabelle.at[zeilezelle, spaltezelle] >= 1:
            listexy = [zeilezelle, spaltezelle]
            with open(dateiname, 'a', encoding='utf-8') as csv_schreib_datei:
                writer = csv.writer(csv_schreib_datei)
                writer.writerow(listexy)

    
                
        
# Print Ausgaben am Ende der Simulation
os.system('clear')


print(tabelle)
print('================================================================')

print('\n\nAnzahl Aktualisierungsdurchgänge: ', counter)
print('''
Zeilen, Spalten: ''', zeilen, spalten, '''
alpha = ''', alpha, '''
beta = ''', beta, '''
gamma = ''', gamma)
print('Berechnungszeit: ', zeit)