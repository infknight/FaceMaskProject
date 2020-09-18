import cv2

# create a video capture thing and use parameter 0 for default camera
cap = cv2.VideoCapture(0)

# use a inf loop to capture frame
while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # this will show in the window
    cv2.imshow("video frame", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

