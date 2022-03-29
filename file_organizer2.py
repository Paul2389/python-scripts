#! Python3
#

from logging import exception
import os
import time
import shutil

VIDEO_FORMATS = [".mp4"," .avi", ".mpeg",".webm", ".mkv"]
PICTURE_FORMATS = [".jpg", ".jpeg", ".png",".gif", ]

HOME = os.path.expanduser('~/')
DOWNLOADS = os.path.expanduser('~/Downloads/')
VIDEOS = os.path.expanduser('~/Videos/')
PICTURES = os.path.expanduser('~/Pictures/')
YT_DL = os.path.expanduser('~/youtube-dl/')

fcount = 1

def compare_fnames(selected, destination, fformatt):  
    global fcount
    try:
        for file in os.listdir(selected):
            fname = file.split('.')[0]
            ext =  '.' + file.split('.')[-1]

            if ext in fformatt:

                if os.path.isfile(destination + file):
                    #time.sleep(300)
                    new_fname = fname + '-' + str(fcount) + ext
                    print(f'- filename: {file} already exists \n- in: {destination+file}')

                while os.path.isfile(destination + file):
                    time.sleep(0.5)
                    new_fname = fname + '-' + str(fcount) + ext
                    print(f'+ Renaming filename to: {new_fname}')

                    if os.path.isfile(destination + new_fname) is False:
                        shutil.move(selected + file, destination + new_fname)
                        print(f'-> New filename is: {new_fname}')
                        break

                    fcount += 1
                else:
                    shutil.move(selected + file, destination + file)
                    print(f'Moving file to:{destination}')
    except exception as e:
        print(e)


while True:
    time.sleep(20)
    compare_fnames(DOWNLOADS, VIDEOS, VIDEO_FORMATS)
    compare_fnames(DOWNLOADS, PICTURES, PICTURE_FORMATS)
    compare_fnames(HOME, YT_DL, VIDEO_FORMATS)
    #time.sleep(60)