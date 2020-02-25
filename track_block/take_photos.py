import cv2
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")
f = open("bg.txt", "a")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 112:
        onlyfiles = next(os.walk("positives"))[2]
        img_name = "positives/pos_{}.jpg".format(len(onlyfiles) + 1)
        print("Positive taken")
        cv2.imwrite(img_name, frame)

    elif k%256 == 110:
        onlyfiles = next(os.walk("negatives"))[2]
        img_name = "negatives/neg_{}.jpg".format(len(onlyfiles) + 1)
        f.write("negatives/neg_{}.jpg\n".format(len(onlyfiles) + 1))
        print("Negative taken")
        cv2.imwrite(img_name, frame)
        

cam.release()
cv2.destroyAllWindows()
f.close()
