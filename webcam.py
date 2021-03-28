import cv2


def takeSnap():
    CaptureObject = cv2.VideoCapture(0)

    result = True
    while (result):
        ret,frame = CaptureObject.read()

        cv2.imwrite("Picture1.png", frame)
        result = False

    CaptureObject.release()

    cv2.destroyAllWindows()
takeSnap()