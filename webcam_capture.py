import cv2, time

#Video Object with Video Capture Method, 0 index argument sense we only have 1 webcam.
video=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    #NumPy Array that displays BGR pixel output of each frame of the video. 
    check, frame=video.read()

    print(check)
    print(frame)

    #convert image to gray
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #After webcam triggering, it will wait for 3 seconds.
    #time.sleep(3)

    #Creating the first frame of the video. 
    cv2.imshow("Capturing", frame)

    #press any key and the process stops
    key=cv2.waitKey(1)
    
    #stop the program by stop pressing Q on the keyboard
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()