import cv2
from cv2 import VideoCapture
def grayScale(r:int,g:int,b:int)-> int:
    return int(r*0.2126+g*0.7152+b*0.0722)//3
videoWebcam = VideoCapture(0)
while True:
    valeurRetour, imageWebcam = videoWebcam.read()
    
    for j in range(imageWebcam.shape[0]):
        for i in range(imageWebcam.shape[1]):
            r,g,b = imageWebcam[j][i]
            imageWebcam[j][i]= grayScale(r,g,b)
    cv2.imshow('Rendu de la caméra avec le filtre', imageWebcam)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
videoWebcam.release()
cv2.destroyAllWindows() 

