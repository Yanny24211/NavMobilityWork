import os
from os import listdir
from datetime import datetime
from PIL import Image 
from PIL.ExifTags import TAGS
import shutil
import cv2

#Returns the time the photo was taken using exif tags

def date_taken(path):
    time_taken = Image.open(path)._getexif()[36867]
    return time_taken[11:16] \

def sort_file(file_name, date):
    hour = int(date [0:2])
    min = int(date[3:5])
    dayPath = r"C:\Users\Yanny\Desktop\NavMobility Interview\DayNight\day"
    nightPath = r"C:\Users\Yanny\Desktop\NavMobility Interview\DayNight\night"
    srcPath = file_name  
    if (hour >= 19 and min >= 30):
        shutil.copy(srcPath, nightPath)
    else: 
        shutil.copy(srcPath, dayPath) 

def compare():
    dayPath = r"C:\Users\Yanny\Desktop\NavMobility Interview\DayNight\day"
    nightPath = r"C:\Users\Yanny\Desktop\NavMobility Interview\DayNight\night"
    file = open("results.txt", "w+")
    for folder in [dayPath, nightPath]:
        images = os.listdir(folder)
        for i in range(len(images)-1):
            img1 = cv2.imread(os.path.join(folder, images[i]))
            img2 = cv2.imread(os.path.join(folder, images[i+1]))
            img1 = cv2.GaussianBlur(img1, (5, 5), 0)
            img2 = cv2.GaussianBlur(img2, (5, 5), 0)
            diff = cv2.absdiff(img1, img2)
            file.write("\nImages " + str(i) + " and " + str(i+1) + "\n")
            file.write(str(diff))   

#Could add a clear function to empty the folders and reset the results so that program can be run for multiple folders of images
            
folder_dir = r"C:\Users\Yanny\Desktop\NavMobility Interview\DayNight\org"
image_types = ('.png', '.jpeg', '.jpg', '.gif')
    
def main():
    #creates final dirs for sorting
    for images in os.listdir(folder_dir):
        imagesFile = r"C:\Users\Yanny\Desktop\NavMobility Interview\DayNight\org"'\\'
        name = imagesFile + images
        time = date_taken(name)
        sort_file(name, time)
        compare()


if __name__ == "__main__":
    main()


