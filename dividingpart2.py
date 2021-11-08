import cv2
import os
vidcap = cv2.VideoCapture(r'C:\Users\Shreeyash\OneDrive\Desktop\folder\video.3gp')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(str(count)+".jpg", image)     # save frame as JPG file
    else : print('error')
    return hasFrames
sec = 0
frameRate = (0.5) #//it will capture image in each 1/24 second
count=1
success = getFrame(sec)
while success:
    print(count)
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
def merging(imagename,imcount):
    directory = 'C:/Users/Shreeyash/OneDrive/Desktop/folders'
    #path = 'C:/Users/Shreeyash/OneDrive/Desktop/folder/20ran.jpg'
    st=''
    for im in imagename:
        if im.isdigit():st=st+im
    imnum=int(st)
    threshold=4# I took threshold as 48 so 48 images before the matched image and 48 after matched 
    lowerth=imnum-threshold#I just took lower threshold and upper threshold to keep the code understandable
    upperth=imnum+threshold
    img_array = []
    i=lowerth
    #print('if')
    filename=str(i)+'.jpg'
    imstr=filename.split('.')
    while ((imstr[0] == str(i)) and (i<=upperth)):
        print(i,filename)
        img = cv2.imread(os.path.join(directory,filename))
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
        i+=1
        filename=str(i)+'.jpg'
        imstr=filename.split('.')
    out = cv2.VideoWriter('project.3gp',cv2.VideoWriter_fourcc(*'DIVX'), 2, size)#here i kept fps as 24 coz we split a frame every 1/24 sec.This value should change acoording to dividing program
    for j in range(len(img_array)):
        out.write(img_array[j])
    out.release()#This will store the video in the directory where you stored the program

merging('20.jpg',197)
