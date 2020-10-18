import cv2
import keyboard
import os

w=100
h=100
x1=0
y1=0
x2=w
y2=h
count=0
record=False
dataCount=len(os.listdir('./Human Hand/'))-1
cap = cv2.VideoCapture(0)
frameCount=0
while(True):
    frameCount=frameCount+1
    if frameCount>1000:
        frameCount=0
    _, frame = cap.read()
    frame=cv2.flip(frame,1)    
    frame=cv2.resize(frame,(650,650))
    
    #############Dealing With Key Presses Starts################
    if(keyboard.is_pressed('w')):#up
        y1=y1-2
        y2=y2-2
        if(y1<0):
            y1=0
            y2=h
    elif(keyboard.is_pressed('s')):#down
        y1=y1+2
        y2=y2+2
        if(y2>650):
            y1=650-h
            y2=650
    elif(keyboard.is_pressed('a')):#left
        x1=x1-2
        x2=x2-2
        if(x1<0):
            x11=0
            x2=w
    elif(keyboard.is_pressed('d')):#down
        x1=x1+2
        x2=x2+2
        if(x2>650):
            x1=650-w
            x2=650
    elif(keyboard.is_pressed('1')):#height up
        h=(h+2)
        y2=y2+2
        if y2>650:
            y2=y2-2
            h=h-2
    elif(keyboard.is_pressed('2')):#height down
        h=(h-2)
        if(h<2):
            h=2
        y2=y1+h    
    elif(keyboard.is_pressed('3')):#width up
        w=(w+2)
        x2=x2+2
        if x2>650:
            x2=x2-2
            w=w-2                
    elif(keyboard.is_pressed('4')):#width down
        w=(w-2)
        if(w<2):
            w=2
        x2=x1+w
    elif(keyboard.is_pressed('r')):#width down
        record=True
    elif(keyboard.is_pressed('p')):#width down
        record=False
    #############Dealing With Key Presses Ends################
    
    #cv2.rectangle(image, start_point, end_point, color, thickness)
    if(frameCount%2==0):
        frame=cv2.rectangle(frame, (x1,y1), (x2,y2), (25,0,0), 3)
    
    frame=cv2.putText(frame,f'Record:{record}  data: {dataCount}',(20,20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0 ),5)
    
    if record==True and frameCount%2!=0:
        cv2.imwrite('./Human Hand/M'+str(dataCount)+'.jpg',frame)
        f= open("./Human Hand/Label/M"+str(dataCount)+'.txt',"w+")
        f.write(f'Human hand {x1} {y1} {x2} {y2}')
        dataCount=dataCount+1
    cv2.imshow('frame',frame)
    #-Loop Breaking Key Check-
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord("q"):
        break
    ##########################

cap.release()
cv2.destroyAllWindows()