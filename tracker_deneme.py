import cv2

################################################# 
#tracker = cv2.TrackerMOSSE_create()
#tracker = cv2.TrackerCSRT_create()
#tracker = cv2.TrackerMedianFlow_create()
#tracker = cv2.TrackerMIL_create()
##################################################

cap = cv2.VideoCapture(0)
success, img = cap.read()
bbox = None

while True:

    success, img = cap.read()
    
    if bbox is not None:
        (success, bbox) = tracker.update(img)
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(img, (x,y),(x+w,y+h), (0,0,255),2,cv2.FONT_HERSHEY_SIMPLEX)
        cv2.putText(img,'Takip kontolu:' 'basarili' if success else 'Takip kontrolu: basarisiz',(20,30),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
        cv2.imshow('Takipci', img)
    else:
        cv2.putText(img,'Secim yapmak icin s tusuna bas!',(60,60), cv2.FONT_HERSHEY_SIMPLEX,1,(255,55,0), 2)
        cv2.imshow('Bekleniyor',img)

        if cv2.waitKey() & 0xff == ord('s') :
            bbox = cv2.selectROI('Secim',img, False)
            tracker.init(img, bbox)
            cv2.destroyAllWindows()

    if cv2.waitKey(2) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
