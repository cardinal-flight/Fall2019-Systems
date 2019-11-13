# import cv2

# pic_path = 'C:\\users\david\Pictures\David Eddy ID.jpg'

# my_pic = cv2.imread(pic_path, cv2.IMREAD_COLOR)
# cv2.imshow('image', my_pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Using matplotlib to display
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import pdb
# import time

# start_time = time.time()
# pic_path = 'C:\\users\david\Pictures\David Eddy ID.jpg'
# my_pic = cv2.imread(pic_path, 0)
# for i in range(len(my_pic)):
    # for j in range(len(my_pic[0])):
        # if my_pic[i][j] < 60:
            # my_pic[i][j] = 0
        # else:
            # my_pic[i][j] = 100
# # pdb.set_trace()
# plt.imshow(my_pic, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])
# print(time.time() - start_time)
# plt.show()


# Live-stream video to grayscale
import numpy as np
import cv2
import pdb
import matplotlib.pyplot as plt

print('imports complete')

vid_capture = cv2.VideoCapture(0)

this = True
while this:
    # Capture frame-by-frame
    ret, frame = vid_capture.read()
    
    # Our operations on the frame come here
    for i in range(150, len(frame)-150):
        for j in range(200, len(frame[0])-200):
            if sum(frame[i][j]) < 100:
                frame[i][j][0] = 0
                frame[i][j][1] = 0
                frame[i][j][2] = 0
            elif sum(frame[i][j]) < 300:
                frame[i][j][0] = 100
                frame[i][j][1] = 100
                frame[i][j][2] = 100
            else:
                frame[i][j][0] = 255
                frame[i][j][1] = 255
                frame[i][j][2] = 255
    
    # Flip the video (0 to flip horizontally, 1 to flip vertically)
    frame = cv2.flip(frame,1)
    # Change the color to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('frame', gray)
    
    # # Matplotlib plotting
    # plt.imshow(frame, cmap='gray', interpolation='bicubic')
    # plt.xticks([]), plt.yticks([])
    # plt.show()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid_capture.release()
cv2.destroyAllWindows()