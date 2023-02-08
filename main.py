import cv2
from cv2 import VideoCapture

videoWebcam = VideoCapture(0)
while True:
    valeurRetour, imageWebcam = videoWebcam.read()
    gray = cv2.cvtColor(imageWebcam, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Rendu de la caméra avec le filtre', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
videoWebcam.release()
cv2.destroyAllWindows()
