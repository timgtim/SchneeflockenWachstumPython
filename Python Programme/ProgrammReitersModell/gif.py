from PIL import Image
import os, shutil

def gifErstellen(pfad):
    geschwindigkeit_in_millisekunden = 200  # Erhöhen Sie diesen Wert für eine langsamere Animation


    # Pfad zum Ordner mit den Bildern
    bilder_verzeichnis = str(pfad)

    # Liste der Dateinamen der Bilder im Ordner
    bilder_dateien = sorted(os.listdir(bilder_verzeichnis))
    bilder_dateien.sort(key=lambda x: int(x.split('.')[0]))

    #Bilder öffnen und zur gif-Liste hinzufügen
    gif_bilder = []
    for datei_name in bilder_dateien:
        bild_pfad = os.path.join(bilder_verzeichnis, datei_name)
        bild = Image.open(bild_pfad)
        gif_bilder.append(bild)
    speicherGif = pfad[0:-9]
    
    #gif Speichern
    gif_bilder[0].save(speicherGif + 'SchneeflockeAnimation.gif', save_all=True, append_images=gif_bilder[1:], duration=geschwindigkeit_in_millisekunden, loop=0)
    
    löschen = input('''
Sollen die Dateien für das Erstellen vom Gif gelöscht werden? 
(1) Ja
(2) Nein ''')
    
    if löschen == '1':
        dirPath = str(bilder_verzeichnis)
        shutil.rmtree(dirPath)
        verzeichnisGif = bilder_verzeichnis[:-9] + 'GifOrdner'
        shutil.rmtree(verzeichnisGif)
    print('Gif erstellt!')

if __name__ == "__main__":
    a = 1
