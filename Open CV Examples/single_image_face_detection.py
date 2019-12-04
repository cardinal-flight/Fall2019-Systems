# Face detection in still frames
import cv2
import image_helpers

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
# img = cv2.imread('cage.jpg')
# img = cv2.imread('brandlmotors.jpg')
# img = cv2.imread('colton_woods.jpg')
# img = cv2.imread('FB_IMG_1480340563735.jpg')
# img = cv2.imread('FB_IMG_1480340557410.jpg')
# img = cv2.imread('bottom.jpg')
# img = cv2.imread('top.jpg')
# img = cv2.imread('left.jpg')
img = cv2.imread('right.jpg')
dimensions = img.shape
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
image_helpers.camera_move_direction(faces, dimensions)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', (int(dimensions[1]/2),int(dimensions[0]/2)))
cv2.moveWindow('img', 100, 100)
cv2.imshow('img', img)
cv2.waitKey()