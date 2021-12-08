import cv2
from random import randrange

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
# img = cv2.imread('couple.jpg')

## To capture video from the webcam
webcam = cv2.VideoCapture(0)

#Iterate forever over frames
while True:
    #### Read the current frame
    successful_frame_read, frame = webcam.read()

    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the face
    # Looping through every face within an image
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 10)

    cv2.imshow('Hillary Omondi face detector', frame)
    key = cv2.waitKey(1)

    #### Stop if Q is press
    #values have been captured from the ascii table
    if key == 81 or key == 113:
        break

#### Release the VideoCapture object
webcam.release()

"""

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the face
#Looping through every face within an image
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 10)


#print(face_coordinates)

#Display the image with the faces
cv2.imshow("Hillary Omondi face detector", img)

#Waits until a key is pressed to terminate the displayed image
cv2.waitKey()

"""

print("code completed")
