import cv2
from scipy.spatial import distance as dist

cap = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    status , photo = cap.read()
    face_cor = face_model.detectMultiScale(photo)
    l = len(face_cor)
    photo = cv2.putText(photo, str(len(face_cor))+" Face", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)
    stack_x = []
    stack_y = []
    stack_x_print = []
    stack_y_print = []
    global D

    if len(face_cor) == 0:
        pass
    else:
        for i in range(0,len(face_cor)):
            x1 = face_cor[i][0]
            y1 = face_cor[i][1]
            x2 = face_cor[i][0] + face_cor[i][2]
            y2 = face_cor[i][1] + face_cor[i][3]

            mid_x = int((x1+x2)/2)
            mid_y = int((y1+y2)/2)
            stack_x.append(mid_x)
            stack_y.append(mid_y)
            stack_x_print.append(mid_x)
            stack_y_print.append(mid_y)

            photo = cv2.circle(photo, (mid_x, mid_y), 3 , [255,0,0] , -1)
            photo = cv2.rectangle(photo , (x1, y1) , (x2,y2) , [0,255,0] , 2)

        if len(face_cor) == 2:
            D = int(dist.euclidean((stack_x.pop(), stack_y.pop()), (stack_x.pop(), stack_y.pop())))
            photo = cv2.line(photo, (stack_x_print.pop(), stack_y_print.pop()), (stack_x_print.pop(), stack_y_print.pop()), [0,0,255], 2)
        else:
            D = 0

        if D<250 and D!=0:
            photo = cv2.putText(photo, "!!MOVE AWAY!!", (100, 100), cv2.FONT_HERSHEY_SIMPLEX,2, [0,0,255] , 4)

        photo = cv2.putText(photo, str(D/10) + " cm", (300, 50), cv2.FONT_HERSHEY_SIMPLEX,
                   1, (255, 0, 0) , 2, cv2.LINE_AA)

        cv2.imshow('hi' , photo)
        if cv2.waitKey(100) == 13:
            break

cv2.destroyAllWindows()

