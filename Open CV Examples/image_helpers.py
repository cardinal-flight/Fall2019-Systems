
def camera_move_direction(faces, dimensions):
    if len(faces) == 1:
        x, y, w, h = faces[0][0], faces[0][1], faces[0][2], faces[0][3]
        xw, yw = dimensions[1], dimensions[0]
        face_center = [x + (w/2), y + (h/2)]
        image_center = [xw/2, yw/2]
        if face_center[0] > image_center[0]:
            print('Go Right')
        elif face_center[0] < image_center[0]:
            print('Go Left')
        if face_center[1] > image_center[1]:
            print('Go Down')
        elif face_center[1] < image_center[1]:
            print('Go Up')
    elif len(faces) > 1:
        print('More than one face identified!')
        i_max = 0 # iteration where max area occurs
        a_max = 0 # Max area
        for i in range(len(faces)):
            x, y, w, h = faces[i][0], faces[i][1], faces[i][2], faces[i][3]
            if w*h > a_max:
                a_max = w*h
                i_max = i
            xw, yw = dimensions[1], dimensions[0]
            face_center = [x + (w/2), y + (h/2)]
            image_center = [xw/2, yw/2]
            if face_center[0] > image_center[0]:
                print('Go Right')
            elif face_center[0] < image_center[0]:
                print('Go Left')
            if face_center[1] > image_center[1]:
                print('Go Down')
            elif face_center[1] < image_center[1]:
                print('Go Up')
    elif len(faces) == 0:
        print('Nothing detected!')