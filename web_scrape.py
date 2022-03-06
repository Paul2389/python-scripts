#! Python3
# dl.py - image -video downloader

from bs4 import BeautifulSoup
import requests
import argparse
import os


#Global count
vid_count = 0
img_count = 0


#url
parser = argparse.ArgumentParser()
parser.add_argument('link', metavar='link', type=str)
args = parser.parse_args()
url = args.link


#Get web title
req = requests.get(url, timeout=1).text
bsoup = BeautifulSoup(req, 'html.parser')
website_title = bsoup.title.string

#multi-os expanduser to Downloads folder
path = os.path.expanduser('~/Downloads/PyDownloads/')
#folder and destination
folder = '-'.join(website_title.replace(' ', '').split('-')[:-1])
destination = path + folder + "/"

#check if folder exists and create new
if os.path.isdir(destination) is not True:
    print('Creating New Folder...',path + folder)
    os.mkdir(destination)

else:
    print('Folder Name Already Exists.')
    

"""Functions"""
def web_data(url):
    req = requests.get(url, timeout=1).text
    bsoup = BeautifulSoup(req, 'html.parser')
    return bsoup


def video_download(bsoup):
    global vid_count

    for video in bsoup.find_all('video'):
        vid_link = video.source['src']
        vid_count += 1
        vid_fname = folder.split('-')[0]

        #Save Files
        with open (destination + vid_fname + '-video-' + str(vid_count) + '.mp4', 'wb') as f:
            req = requests.get(vid_link, timeout=1)
            print('Downloading Video', vid_count, '...')
            f.write(req.content)
            print('Video', vid_count, 'Saved!')
            print("++++++++++++++++++")

def image_download(bsoup):
    global img_count

    for image in bsoup.find_all('img', class_= 'alignleft'):
        img_link = image['src']
        img_count += 1
        img_fname = folder.split('-')[0]

        with open (destination + img_fname + '-image-' + str(img_count) + '.jpg', 'wb') as f:
            req = requests.get(img_link, timeout=1)
            print('Downloading Image', img_count, '...')
            f.write(req.content)
            print('Image', img_count, 'Saved!')
            print("++++++++++++++++++")


def next_page(soup):    
    # find tags, elements of Next Page
    current_page = soup.find('span', class_= 'post-page-numbers current')
    # if there are more than 1 paiges
    if current_page != None:
        # if last page
        if not current_page.findNext('a', class_= 'post-page-numbers'): # find next sibling
            print('End of Pages.')
            return 
        else:
            # if next page , get link  
            url = current_page.findNext('a', class_= 'post-page-numbers')['href'] # find next sibling
            print('New Page Found...')        
            return url
    else:
        # there are no more than 1 pages
        return
while True:
    web_data(url)
    bsoup = web_data(url)
    video_download(bsoup)
    image_download(bsoup)
    url = next_page(bsoup)
    if not url:
        print("Finished." ,img_count, "Images and", vid_count, "Videos Downloaded.")
        break