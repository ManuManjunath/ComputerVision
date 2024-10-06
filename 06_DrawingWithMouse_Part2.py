import numpy as np
import cv2

blank_img = np.zeros(shape= (512, 512, 3))
windowName = "Custom Drawing"

# Function for drawing
def draw_circle(event, x, y, flags, param):
    pass

cv2.namedWindow(winname = windowName)
cv2.setMouseCallback(windowName, draw_circle)

while True:
    cv2.imshow(windowName, blank_img)

    if (cv2.waitKey(2000) & 0xFF == 27):
        break

cv2.destroyAllWindows()