import os
import time
import shutil

VIDEO_FORMATS = ["mp4"," avi", "mpeg"," webm"]
PICTURE_FORMATS = ["jpg", "jpeg", "png","gif", ]

HOME = os.path.expanduser('~/')
DOWNLOADS = os.path.expanduser('~/Downloads/')
VIDEOS = os.path.expanduser('~/Videos/')
PICTURES = os.path.expanduser('~/Pictures/')
YT_DL = os.path.expanduser('~/youtube-dl/')

while True:
    #From Downloads folder
    for file in os.listdir("/home/user28/Downloads"):
        i =1
        filename = file.split(".")[0]
        extension = file.split(".")[-1]

        #VIDEOS
        if os.path.isfile(DOWNLOADS + file): 
            if extension in VIDEO_FORMATS:
                file_exist = os.path.isfile(VIDEOS + file)

                while file_exist:
                    print("Duplicate found.")
                    newname = filename+"-"+str(i)+"."+extension
                    newfile_exist = os.path.isfile(VIDEOS +newname)
                    time.sleep(1)
                    if newfile_exist is False:
                        shutil.move(DOWNLOADS + file, VIDEOS + newname)
                        print("Creating new file")
                        break
                    i+=1    
                else:
                    shutil.move(DOWNLOADS + file, VIDEOS + file)
                    print("Success File Moved")

        #PICTURES
        if os.path.isfile(DOWNLOADS + file): 
            if extension in PICTURE_FORMATS:
                file_exist = os.path.isfile(PICTURES + file)

                while file_exist:
                    print("Duplicate found.")
                    newname = filename+"-"+str(i)+"."+extension
                    newfile_exist = os.path.isfile(PICTURES + newname)
                    time.sleep(1)
                    if newfile_exist is False:
                        shutil.move(DOWNLOADS+ file, PICTURES + newname)
                        print("Creating new file")
                        break
                    i+=1    
                else:
                    shutil.move(DOWNLOADS+ file, PICTURES + file)
                    print("Success File Moved")

    for file in os.listdir(HOME):
        i =1
        filename = file.split(".")[0]
        extension = file.split(".")[-1]

        #YT-DL
        if os.path.isfile(HOME + file): 
            if extension in VIDEO_FORMATS:
                file_exist = os.path.isfile(YT_DL + file)

                while file_exist:
                    print("Duplicate found.")
                    newname = filename+"-"+str(i)+"."+extension
                    newfile_exist = os.path.isfile(YT_DL +newname)
                    time.sleep(1)
                    if newfile_exist is False:
                        shutil.move(HOME + file, YT_DL + newname)
                        print("Creating new file")
                        break
                    i+=1    
                else:
                    shutil.move(HOME + file, YT_DL + file)
                    print("Success File Moved")
    time.sleep(60)
