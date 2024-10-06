import numpy as np
import cv2

blank_img = np.zeros(shape= (512, 512, 3))
windowName = "Custom Drawing"

drawing = False
ix, iy = -1, -1

# Function for drawing
def draw_circle(event, x, y, flags, param):
    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(blank_img, pt1 = (ix, iy), pt2 = (x, y), color = (255, 255, 255), thickness = -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
        cv2.rectangle(blank_img, pt1 = (ix, iy), pt2 = (x, y), color = (255, 255, 255), thickness = -1)

cv2.namedWindow(winname = windowName)
cv2.setMouseCallback(windowName, draw_circle)

while True:
    cv2.imshow(windowName, blank_img)

    if (cv2.waitKey(2000) & 0xFF == 27):
        break

cv2.destroyAllWindows()