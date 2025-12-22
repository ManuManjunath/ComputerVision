import cv2
import time

cap = cv2.VideoCapture("webcam.mp4")

if cap.isOpened() == False:
    print("Error opening file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # To show the video in the original frame rate
        time.sleep(1/20)
        # 20 was the fps for the recorded video
        cv2.imshow("frame", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()