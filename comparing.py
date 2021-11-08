#here is a  code where i merged the images it also includes comapring of the images 
#Before running this i made sure that the dividing program stores the names of the images starting with numbers as the name of images
#For a 98 sec video it took around 15min to split images and roughly 4 mins to compare and merge 
import os
import cv2
#definition of the function merge
def merging(imagename,imcount):
    directory = 'C:/Users/Shreeyash/OneDrive/Desktop/folder'
    #path = 'C:/Users/Shreeyash/OneDrive/Desktop/folder/20ran.jpg'
    st=''
    for im in imagename:
        if im.isdigit():st=st+im
    imnum=int(st)
    threshold=48# I took threshold as 48 so 48 images before the matched image and 48 after matched 
    lowerth=imnum-threshold#I just took lower threshold and upper threshold to keep the code understandable
    upperth=imnum+threshold
    img_array = []
    i=lowerth
    if lowerth>0 and upperth<imcount:
        print('if')
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
    elif lowerth<=0:
        lowerth=1
        tempth=threshold-imnum
        upperth=upperth+tempth
        i=lowerth
        print('lowerth',lowerth,'upperth',upperth,'threshold',threshold,'i',i,'tempth',tempth)
        filename=str(i)+'.jpg'
        imstr=filename.split('.')
        while ((imstr[0] == str(i)) and (i<=upperth)):
            print(i,filename)
            img = cv2.imread(os.path.join(directory,filename))
            #print(filename)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
            i+=1
            filename=str(i)+'.jpg'
            imstr=filename.split('.')
    elif upperth>=imcount:
        upperth=imcount
        tempth=threshold-(imcount-imnum)
        lowerth=lowerth-tempth
        i=lowerth
        print('lowerth',lowerth,'upperth',upperth,'threshold',threshold,'i',i,'tempth',tempth)
        filename=str(i)+'.jpg'
        imstr=filename.split('.')
        while ((imstr[0] == str(i)) and (i<=upperth)):
            print(i,filename)
            img = cv2.imread(os.path.join(directory,filename))
            #print(filename)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
            i+=1
            filename=str(i)+'.jpg'
            imstr=filename.split('.')
        
    out = cv2.VideoWriter('project.3gp',cv2.VideoWriter_fourcc(*'DIVX'), 24, size)#here i kept fps as 24 coz we split a frame every 1/24 sec.This value should change acoording to dividing program
    for j in range(len(img_array)):
        out.write(img_array[j])
    out.release()#This will store the video in the directory where you stored the program

directory = 'C:/Users/Shreeyash/OneDrive/Desktop/folder'
path = 'C:/Users/Shreeyash/OneDrive/Desktop/folder/1731.jpg'
test_image = cv2.imread(path,1)
gray_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
histogram1 = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
count,imc=0,0
min=10000000000
i=1
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith('.jpg'):    
        img = cv2.imread(os.path.join(directory,filename))
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        histogram=(cv2.calcHist([gray_image], [0], None, [256], [0, 256]))
        c=0
        i = 0
        while i<len(histogram) and i<len(histogram1):
            c=c+(histogram[i]-histogram1[i])**2
            i+= 1
        c = c**(1 / 2)
        if filename == 'ran20.jpg':
            print(filename,'c:',c)
        if(min>c):
            min=c
            filename1=filename
            count=count+1
            print(filename,'c:',min)
        imc+=1
print(filename1+"is more similar to test.jpg")
print(count,imc)
merging(filename1,imc)