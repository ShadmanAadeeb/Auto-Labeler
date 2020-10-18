import cv2
import os

######INSTRUCTIONS####################
#Make a folder called Human Hand and place all the images there
#Inside the same folder make another folder Label and place all the txt files there
#Run the scipt to check for proper labelling


filenames=os.listdir('./Human hand/')
imgNames=[]
for filename in filenames:
    if filename.endswith('.jpg'):
        imgNames.append(filename[:-4])

for imageName in imgNames:
    img=cv2.imread('./Human hand/'+imageName+'.jpg')
    txt=open('./Human hand/Label/'+imageName+'.txt')
    for line in txt:
        words=line.split()
        x1=int(float(words[2]))
        y1=int(float(words[3]))
        x2=int(float(words[4]))
        y2=int(float(words[5]))
        img = cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,0), 2)
    cv2.imshow('img',img)
    cv2.waitKey(0)


cv2.imshow('img',img)
cv2.waitKey(0)