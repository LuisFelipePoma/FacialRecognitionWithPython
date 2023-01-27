import cv2 as cv

capturaVideo = cv.VideoCapture(0)
if not capturaVideo.isOpened():
    print("No se encontro una camara")
    exit()
else:
    print("Se conecto correctamente con la camara.")
while True:
    tipocamara, Camara = capturaVideo.read()
    grises = cv.cvtColor(Camara, cv.COLOR_BGR2GRAY)
    print(tipocamara)
    cv.imshow("En vivo", grises)
    if cv.waitKey(1) == ord("q"):
        break
capturaVideo.release()
cv.destroyAllWindows()
