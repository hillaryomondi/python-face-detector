import cv2

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
img = cv2.imread('magak.jpg')

# Must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the face
(x, y, w, h) = face_coordinates[0]

cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 10)


#print(face_coordinates)

#
cv2.imshow("Hillary Omondi face detector", img)
#Waits until a key is pressed to terminate the displayed image
cv2.waitKey()

print("code Completed")
