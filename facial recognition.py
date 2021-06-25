import cv2
from os.path import  isfile,join
from os import listdir
import numpy as np
# test 
sample_data='C:/Users/Vijay/Desktop/Image/'
files=[x for x in listdir(sample_data) if isfile(join(sample_data,x))]

TrainData,labels=[],[]

for x,y in enumerate(files):
    imgDir=sample_data+files[x]
    images=cv2.imread(imgDir,cv2.IMREAD_GRAYSCALE)
    TrainData.append(np.asarray(images,dtype=np.uint8))
    labels.append(x)


labels=np.asarray(labels,dtype=np.int32)
model=cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(TrainData),np.asarray(labels))

print("Model Training Complete!!")

#<--training section over

#recognition part -->



#use your own file location here
face_classifier=cv2.CascadeClassifier('C:/Users/Vijay/AppData/Roaming/Python/Python37/site-packages/~v2/data/haarcascade_frontalface_default.xml')
 
print("Press enter or q to exit")
def detector(img,size=0.5):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.1,4)

    if faces is():
        return img,[]

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,255),2)
        region=img[y:y+h,x:x+w]
        region=cv2.resize(region,(250,250))

    return img,region

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)


while True:

    val,frame=cap.read()

    image,face=detector(frame)

    #error handling

    try:
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        result=model.predict(face)

        if(result[1]<500):
            conf=int(100*(1-(result[1])/300))
            txt=str(conf)+'% Accuracy of User'
        cv2.putText(image, txt,(150,55),cv2.FONT_HERSHEY_DUPLEX, 1,(0,200,240),2)
        cv2.imshow("face", image)

        if conf>80:
            cv2.putText(image,"User Identified :)",(200,455),cv2.FONT_ITALIC, 1,(0,255,0),3)
            cv2.imshow("face", image)

        else:
            cv2.putText(image,"User Unidentified !!",(200,455),cv2.FONT_ITALIC, 1,(0,0,255),3)
            cv2.imshow("face", image)


    except:
        cv2.putText(image,"Face Not Found !!",(200,455),cv2.FONT_HERSHEY_DUPLEX, 1,(255,0,0),2)
        cv2.imshow("face", image)
        pass

            

    if cv2.waitKey(1)==13 or cv2.waitKey(1)==113:
        break

cap.release()
cv2.destroyAllWindows()
