import cv2
url = 'http://192.168.0.151:8080/video'
cap = cv2.VideoCapture(url)
while(True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('IP WebCam', frame)
    q = cv2.waitKey(1)
    if q == ord('q'):
        break;
cv2.destroyAllWindows()
