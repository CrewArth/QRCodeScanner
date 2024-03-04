#Import Required Libraries.
import cv2
import numpy as np
from pyzbar.pyzbar import decode

#Setting Up Webcam
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    for qrcodeData in decode(frame):
        myData = qrcodeData.data.decode('utf-8')
        print("QR DATA : ", myData)

        pts = np.array([qrcodeData.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (255,0,0), 5)


        pts2 = qrcodeData.rect
        cv2.putText(frame, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Qr Code Scanner", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()