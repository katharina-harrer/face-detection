import cv2
from matplotlib import pyplot as plt
import glob

COLOR_FACE = (255, 0, 255)  # Farbe für Rahmen ums Gesicht

image_files = glob.glob("*.jpg")  # Alle jpg-Dateien im aktuellen Verzeichnis in Liste speichern

# Für jedes Bild Gesichtserkennung machen
for file in image_files:
    img_bgr = cv2.imread(file, cv2.IMREAD_COLOR)  # Die Bilddatei farbig einlesen
    b, g, r = cv2.split(img_bgr)  # Die Farbwerte auslesen (cv2 erstellt BGR-Bild)
    img_rgb = cv2.merge([r, g, b])  # Aus den BGR-Farbwerten ein RGB-Bild machen
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)  # Ein Graustufenbild für die Erkennung machen

    # Gesichts-Klassifikatoren aus Datei laden
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Eigentliche Gesichtserkennung ausführen
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=5)

    print("Anzahl erkannte Gesichter:", len(faces))  # Anzahl erkannte Gesichter ausgeben

    # Erkannte Gesichter durchgehen.
    # Die erkannten Gesichter werden durch ein umrahmendes Rechteck gegeben:
    # (x, y, w, h) stellen Koordinaten, Breite und Höhe des Rechtecks dar
    for (x, y, w, h) in faces:
        # das Gesicht durch ein farbiges Rechteck im Bild markieren
        cv2.rectangle(img_rgb, (x, y), (x + w, y + h), COLOR_FACE, 5)

    plt.axis('off')  # Diagramm-Achsen ausblenden
    plt.imshow(img_rgb)  # Dem Diagramm das Bild hinzufügen
    plt.title(file)  # Titel des Diagramms setzen
    plt.show()  # Diagramm anzeigen

exit()