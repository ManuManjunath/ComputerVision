import cv2

img_file = "data/00-puppy.jpg"
img = cv2.imread(img_file)

while True:
    cv2.imshow('Puppy', img)

    # Wait 2 seconds AND the "esc" key is pressed
    if (cv2.waitKey(2000) & 0xFF == 27):
        break

    # To close after keeping window open for 2 seconds:
    # if (cv2.waitKey(2000)):

cv2.destroyAllWindows()