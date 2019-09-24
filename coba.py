import cv2.cv as cv
import time

capture = cv.CaptureFromCAM(0)
cv.SetCaptureProperty(capture,3,640)
cv.SetCaptureProperty(capture,4,480)

while True:
    img = cv.QueryFrame(capture)
    cv.Smooth(img,img,cv.CV_BLUR,3)
    #cv.ShowImage("Colour Tracking",img)
    hue_img = cv.CreateImage(cv.GetSize(img),8,3)
    #cv.ShowImage("Colour Tracking",hue_img )
    cv.CvtColor(img,hue_img,cv.CV_BGR2HSV)
    threshold_img=cv.CreateImage(cv.GetSize(img),8,1)
    #cv.ShowImage("Colour Tracking",threshold_img)
    cv.InRangeS(hue_img,(0,150,0),(5,255,255),threshold_img)
    storage = cv.CreateMemStorage(0)
    contour = cv.FindContours(threshold_img,storage,cv.CV_RETR_CCOMP,\
                              cv.CV_CHAIN_APPROX_SIMPLE)
    #cv.ShowImage("Colour Tracking",threshold_img)
    points = []

    while contour:
        rect = cv.BoundingRect(list(contour))
        print rect[0],rect[1]
        contour = contour.h_next()
        size = (rect[2]*rect[3])
        if size > 100:
            pt1 = (rect[0],rect[1])
            pt2 = (rect[0]+rect[2],rect[1]+rect[3])
            cv.Rectangle(img,pt1,pt2,(5,5,255))

    cv.ShowImage("Colour Tracking",threshold_img)
    if cv.WaitKey(10)==27:
        break
