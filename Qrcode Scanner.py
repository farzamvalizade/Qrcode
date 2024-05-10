import cv2
import webbrowser
cap=cv2.VideoCapture(0)
detect=cv2.QRCodeDetector()
while True:
    ret,img=cap.read()
    cv2.imshow("live Video",img)
    data,vert_array,binary_qr=detect.detectAndDecode(img)
    if data:
        b=webbrowser.open(data)
        break
    key=cv2.waitKey(1)
    if key & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
