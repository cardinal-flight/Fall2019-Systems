import pdb

def camera_move_direction(faces, dimensions):
    margin = 0.05 # amount the face is allowed to be off center e.g. 0.1 = 10%
    if len(faces) == 1:
        x, y, w, h = faces[0][0], faces[0][1], faces[0][2], faces[0][3]
        img_x, img_y = dimensions[1], dimensions[0]
        face_center = [x + (w/2), y + (h/2)]
        image_center = [img_x/2, img_y/2]
        # Determine which way to point the camera
        magn = [abs(face_center[0] - image_center[0])/image_center[0]*100, abs(face_center[1] - image_center[1])/image_center[1]*100]
        if face_center[0] > image_center[0] + img_x*margin:
            print('Go Right %.1f' % magn[0])
        elif face_center[0] < image_center[0] - img_x*margin:
            print('Go Left %.1f' % magn[0])
        if face_center[1] > image_center[1] + img_y*margin:
            print('Go Down %.1f' % magn[1])
        elif face_center[1] < image_center[1] - img_y*margin:
            print('Go Up %.1f' % magn[1])
        # pdb.set_trace()
    elif len(faces) > 1:
        i_max = 0 # iteration where max area occurs
        a_max = 0 # Max area
        for i in range(len(faces)):
            x, y, w, h = faces[i][0], faces[i][1], faces[i][2], faces[i][3]
            if w*h > a_max:
                a_max = w*h
                i_max = i
            img_x, img_y = dimensions[1], dimensions[0]
            face_center = [x + (w/2), y + (h/2)]
            image_center = [img_x/2, img_y/2]
            # Determine which way to point the camera
            if face_center[0] > image_center[0] + img_x*margin:
                print('Go Right')
            elif face_center[0] < image_center[0] - img_x*margin:
                print('Go Left')
            if face_center[1] > image_center[1] + img_y*margin:
                print('Go Down')
            elif face_center[1] < image_center[1] - img_y*margin:
                print('Go Up')
    elif len(faces) == 0:
        print('Nothing detected!')