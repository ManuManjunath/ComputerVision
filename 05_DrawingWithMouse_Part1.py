import numpy as np
import cv2

"""
# Tic Tac Toe game!
Use Left Click for Red Circle
Use Right Click for Blue Circle
"""

blank_img = np.zeros(shape= (512, 512, 3))
cv2.line(blank_img, pt1 = (180, 0), pt2 = (180, 512), color = (255, 255, 255), thickness = 2)
cv2.line(blank_img, pt1 = (360, 0), pt2 = (360, 512), color = (255, 255, 255), thickness = 2)
cv2.line(blank_img, pt1 = (0, 180), pt2 = (512, 180), color = (255, 255, 255), thickness = 2)
cv2.line(blank_img, pt1 = (0, 360), pt2 = (512, 360), color = (255, 255, 255), thickness = 2)
windowName = "Custom Drawing"
# Important to use the exact same window name for namedWindow, Callback function and during imshow

# Function for drawing
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(blank_img, center = (x, y), radius = 25, color = (0, 0, 255), thickness = -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(blank_img, center = (x, y), radius = 25, color = (255, 0, 0), thickness = -1)

cv2.namedWindow(winname = windowName)
cv2.setMouseCallback(windowName, draw_circle)

while True:
    cv2.imshow(windowName, blank_img)

    if (cv2.waitKey(2000) & 0xFF == 27):
        break

cv2.destroyAllWindows()