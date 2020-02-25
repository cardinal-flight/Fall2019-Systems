import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

i = 0
vid_frames = []
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()

  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)

    if i % 10 == 0:
      vid_frames.append(frame)

    i += 1
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break

print(len(vid_frames))

out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 5, (640, 480))

for j in range(len(vid_frames)):
  
  out.write(vid_frames[j])
 
# When everything done, release the video capture object
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows()
