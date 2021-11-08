import cv2
import os
directory = 'C:/Users/Shreeyash/OneDrive/Desktop/folder'
path = 'C:/Users/Shreeyash/OneDrive/Desktop/folder/30.jpg'
filename='30.jpg'
def merging():
    directory = 'C:/Users/Shreeyash/OneDrive/Desktop/folder'
    img_array = []
    filename='30.jpg'
    img = cv2.imread(os.path.join(directory,filename))
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    out = cv2.VideoWriter('pro.3gp',cv2.VideoWriter_fourcc(*'DIVX'), 24, size)#here i kept fps as 24 coz we split a frame every 1/24 sec.This value should change acoording to dividing program
    for j in range(len(img_array)):
        out.write(img_array[j])
    out.release()#This will store the video in the directory where you stored the program

merging()
