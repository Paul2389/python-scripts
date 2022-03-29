#! Python3
#
#
import os
import time

DESKTOP = os.path.expanduser('~/Desktop/')
DOWNLOADS = os.path.expanduser('~/Downloads/')

fcount = 1


def compare_fnames(selected, destination):  
    global fcount

    for file in os.listdir(selected):
        
        if os.path.isfile(destination + file):
            fname = file.split('.')[0]
            ext =  '.' + file.split('.')[-1]
            new_fname = fname + '-' + str(fcount) + ext
            print(f'- filename: {file} already exists \n- in: {destination+file}')

            while os.path.isfile(destination + file):
                time.sleep(0.5)
                new_fname = fname + '-' + str(fcount) + ext
                print(f'+ Renaming filename to: {new_fname}')

                if os.path.isfile(destination + new_fname) is False:
                    print(f'-> New filename is: {new_fname}')
                    break

                fcount += 1
            else:
                pass
                
        
compare_fnames(DESKTOP, DOWNLOADS)