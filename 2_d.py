import cv2 
import os

path = ("C:\\Users\\SWEET\\Desktop\\New folder\\loc_folder\\")
out_path =("C:\\Users\\SWEET\\Desktop\\New folder\\loc_folder\\")
out_video_name ='robot.mp4'
out_video_full_path = out_path+out_video_name

pre_imgs =os.listdir(path)
img=[]

for i in pre_imgs:
    i =path+i
    img.append(i)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame= cv2.imread(img[0])
size =list(frame.shape)
del size[2]

video =cv2.VideoWriter(out_video_full_path,cv2_fourcc,24,size)

for i in range(len(img)):
    video.write(cv2.imread(img[i]))

video.release()