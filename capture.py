import cv2
import os
from picamera2 import Picamera2

# Constants
COUNT_LIMIT = 20
POS=(400,35)  # counter top right
FONT=cv2.FONT_HERSHEY_TRIPLEX #font type for text overlay
HEIGHT=1.4  #font_scale
TEXTCOLOR=(255,0,0)  #BGR- BLUE
BOXCOLOR=(0,0,255) #BGR- RED
WEIGHT=2  #font-thickness
FACE_DETECTOR=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n Enter User-id and press enter: ')
print("\n  Initializing face capture. Look at the camera and wait!")

# Create an instance of the PiCamera2 object
cam = Picamera2()
## Set the resolution of the camera preview
cam.preview_configuration.main.size = (640,360)
cam.preview_configuration.main.format = "RGB888"# 24 bits per pixel ordered BGR
cam.preview_configuration.controls.FrameRate=5
cam.preview_configuration.align()
cam.configure("preview")
cam.start()

count=0 # initialize count var to zero

while True:
    # Capture a frame from the camera
    frame=cam.capture_array()
    # Display count of images taken
    cv2.putText(frame,'COUNT:'+str(int(count)),POS,FONT,HEIGHT,TEXTCOLOR,WEIGHT) # text overlay on the display

    # Convert frame from BGR to grayscale  to reduce complexity of code
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Create a DS faces- array with 4 elements- x,y coordinates (top-left corner), width and height
    faces = FACE_DETECTOR.detectMultiScale( # detectMultiScale has 4 parameters return coordinates of bounding box
            frameGray,      # The grayscale frame to detect
            scaleFactor=1.1,# how much the image size is reduced at each image scale-10% reduction
            minNeighbors=5, # how many neighbors each candidate rectangle should have to retain it
            minSize=(30, 30)# Minimum possible object size. Objects smaller than this size are ignored.
    )
    for (x,y,w,h) in faces:
        # Create a bounding box across the detected face
        cv2.rectangle(frame, (x,y), (x+w,y+h), BOXCOLOR, 4) # 5 parameters - frame, topleftcoords,bottomrightcooords,boxcolor,thickness
        count += 1 # increment count

         # if dataset folder doesnt exist create:
        if not os.path.exists("dataset"):
            os.makedirs("dataset")
      # Save the captured bounded-grayscaleimage into the datasets folder only if the same file doesn't exist
        file_path = os.path.join("dataset", f"User.{face_id}.{count}.jpg")
        if os.path.exists(file_path):
            # Move the existing file to the "old_dataset" folder
            old_file_path = file_path.replace("dataset", "old_dataset")
            os.rename(file_path, old_file_path)
        # Write the newer images after moving the old images
        cv2.imwrite(file_path, frameGray[y:y+h, x:x+w])


    # Display the original frame to the user
    cv2.imshow('FaceReader', frame)
    # Wait for 30 milliseconds for a key event (extract sigfigs) and exit if 'ESC' or 'q' is pressed
    key = cv2.waitKey(100) & 0xff
    # Checking keycode
    if key == 27:  # ESCAPE key
        break
    elif key == 113:  # q key
        break
    elif count >= COUNT_LIMIT: # Take COUNT_LIMIT face samples and stop video capture
        break

# Release the camera and close all windows
print("\n [INFO] Exiting Program and cleaning up stuff")
cam.stop()
cv2.destroyAllWindows()
1