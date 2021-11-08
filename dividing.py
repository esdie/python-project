import cv2
vidcap = cv2.VideoCapture(r'C:\Users\Shreeyash\OneDrive\Desktop\folder\video.3gp')
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