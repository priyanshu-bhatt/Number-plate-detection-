#main code
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    gra = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('carpic.jpg',frame)
    cv2.imshow('frame',gra)
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(gra, cv2.COLOR_BGR2RGB))
img=cv2.imread('car11 test.jpeg')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
