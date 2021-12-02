import cv2

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
img = cv2.imread('magak.jpg')

#
cv2.imshow("Hillary omondi face detector", img)

#Waits until a key is pressed to terminate the displayed image
cv2.waitKey()

print("code Completed")
