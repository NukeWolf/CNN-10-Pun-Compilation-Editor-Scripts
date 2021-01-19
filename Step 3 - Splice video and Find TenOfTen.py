#Purpose: After downloading the videos and placing each video in its own folder,
#With names corresponding to integers, this code will go into each folder and splice
# Each video into the last 300 seconds of each video.

import pytesseract
import cv2
import time
import os
import yaml

with open('videos.yaml','r') as f:
    compiledVideos = yaml.load(f,Loader=yaml.FullLoader)
#Final Videos Object
videos = []
#Process the Yaml file into a list in order by Date. The ID value represents the chronological order
for x in range(len(compiledVideos)+1):
    videos.append(1)
for x in compiledVideos:
    print(compiledVideos[x]['id'])
    videos[compiledVideos[x]['id']]=compiledVideos[x]
videos.reverse()
#IDs go from most recent video to oldest video. We reverse so we start in january.


root = os.getcwd()

def saveConfig(videosDict):
    cwd = os.getcwd()
    os.chdir(root)
    config = open('videos.yaml','w')
    yaml.dump(videosDict,config)
    os.chdir(cwd)

#Select main directory as videos. This is created from the last step.
os.chdir("videos")
cwd = os.getcwd()
print(cwd)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def splice(mp4):
    vidcap = cv2.VideoCapture(mp4)
    success,image = vidcap.read()
    for x in range(9000):
        success,image = vidcap.read()
    count = 300
    success = True
    while success:
      cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
      for x in range(30):
          success,image = vidcap.read()
      #print ('Read a new frame: ', success + time.time()-start)
      count += 1

def find10(endFrame):
    for count in reversed(range(300,endFrame)):
        img = cv2.imread('frame%d.jpg' % count)
        text = pytesseract.image_to_string(img)
        if ("10 OUT OF 10" in text):
            return count
    return -1


for index in range(195):
    os.chdir(str(index))
    files = os.listdir()
    print(files[0],index,"Splicing!")
    #Takes the downloaded video in the folder and splices it into 300 jpegs
    splice(files[0])
    print("Finding 10")
    #After splicing, it then proceeds to find the frame where it says 10 out of 10 with OCR and then saves it.
    frameStart = find10(videos[index]['endFrame'])
    #Saves the frame where it starts into the config
    compiledVideos[videos[index]['date']]['startFrame'] = frameStart
    saveConfig(compiledVideos)
    
    os.chdir(cwd)



