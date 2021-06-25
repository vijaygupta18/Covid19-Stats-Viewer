import cv2
import numpy as np

#use your own file location here
face_classifier=cv2.CascadeClassifier('C:/Users/Vijay/AppData/Roaming/Python/Python37/site-packages/~v2/data/haarcascade_frontalface_default.xml')

def face_extractor(image):
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    if faces is():
        return None
    for(x,y,w,h) in faces:
        cropped_f=image[y:y+h,x:x+w]

    return cropped_f


cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
count=0

while True:

    retval,frame=cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face=cv2.resize(face_extractor(frame),(250,250))
        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        #use your own file location here
        filepath='C:/Users/Vijay/Desktop/Image/vijay'+str(count)+'.jpg'
        cv2.imwrite(filepath,face)
        cv2.putText(face,str(count),(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow("faces",face)

    else:
        print("faces are not visibe")  
        pass

    if cv2.waitKey(1)==13 or count==150:
        break

cap.release()
cv2.destroyAllWindows()
print("Samples collected")

