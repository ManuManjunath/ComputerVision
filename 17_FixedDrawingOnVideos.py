import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Top left
x1 = width // 2
y1 = height // 2
x2 = width // 4
y2 = height // 4
# Bottom right = x1+x2, y2+y2

while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (x1, y1), (x1 + x2, y1 + y2), color = (0, 0, 255), thickness = 3)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()