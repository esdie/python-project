import cv2;
import os;
vidcap = cv2.VideoCapture(r'C:\Users\Shreeyash\OneDrive\Desktop\folders\project.3gp')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(str(count)+".jpg", image)     # save frame as JPG file
    else : print('error')
    return hasFrames
sec = 0
frameRate = (1/24) #//it will capture image in each 1/24 second
count=1
success = getFrame(sec)
while success:
    print(count)
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 5)
    success = getFrame(sec)
def merging():
    directory = 'C:/Users/Shreeyash/OneDrive/Desktop/folders'
    img_array = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(directory,filename))
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
    out = cv2.VideoWriter('project.3gp',cv2.VideoWriter_fourcc(*'DIVX'), 24, size)#here i kept fps as 24 coz we split a frame every 1/24 sec.This value should change acoording to dividing program
    for j in range(len(img_array)):
        out.write(img_array[j])
    out.release()#This will store the video in the directory where you stored the program

merging()
