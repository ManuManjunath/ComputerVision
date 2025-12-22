import cv2

cap = cv2.VideoCapture(0)
# 0 --> Default camera

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# Returns decimal. But we would need to work with integers. So casting them as int

# To save the video
writer = cv2.VideoWriter(filename = "webcam.mp4", fourcc = cv2.VideoWriter_fourcc(*'XVID'), fps = 20, frameSize = (width, height))


# Use XVID for Linux or Mac, DIVX for Windows
# 20 is the number of frames per second we're asking to capture

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    # To capture colour video:
    # gray = None
    # cv2.imshow('frame', frame)

    # To write the video to file
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()