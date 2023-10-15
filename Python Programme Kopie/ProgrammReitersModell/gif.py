from PIL import Image
import os

def gifErstellen(pfad):

    # Pfad zum Ordner mit den Bildern
    bilder_verzeichnis = str(pfad)

    # Liste der Dateinamen der Bilder im Ordner
    bilder_dateien = sorted(os.listdir(bilder_verzeichnis))
    bilder_dateien.sort(key=lambda x: int(x.split('.')[0]))

    # Bilder öffnen und zur GIF-Liste hinzufügen
    gif_bilder = []
    for datei_name in bilder_dateien:
        bild_pfad = os.path.join(bilder_verzeichnis, datei_name)
        bild = Image.open(bild_pfad)
        gif_bilder.append(bild)
    speicherGif = pfad[0:-9]
    # Speichern Sie die Bilder als GIF mit einer längeren Dauer (langsamer)
    dauer_in_millisekunden = 200  # Erhöhen Sie diesen Wert für eine langsamere Animation
    gif_bilder[0].save(speicherGif + 'SchneeflockeAnimation.gif', save_all=True, append_images=gif_bilder[1:], duration=dauer_in_millisekunden, loop=0)

    print('Gif erstellt!')

if __name__ == "__main__":
    gifErstellen('Dateien/Animationen/Z100A2.69B0.2G0.4/BilderGif')
