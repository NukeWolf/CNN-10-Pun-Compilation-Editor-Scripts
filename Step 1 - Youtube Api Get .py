import requests
import json
import yaml
from youtube_transcript_api import YouTubeTranscriptApi
from selenium import webdriver
import keyboard

def wait():
    while True:
        if keyboard.is_pressed('q'):
            break

def loadChrome():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb")
    print("Install Adblock, then press Q")
    wait()
    return driver

#Gets the Key
with open('key.txt','r') as f:
    key = f.read()
driver = loadChrome()



#Returns json object of video
def getVideoList(pageToken):
    api = "https://www.googleapis.com/youtube/v3/search"
    channelParams = {
        'key': key,
        'channelId':'UCTOoRgpHTjAQPk6Ak70u-pA',
        'order':'date',
        'maxResults':'50',
        'publishedAfter':'2020-01-01T00:00:00+00:00',
        'pageToken':pageToken
    }
    return requests.get(api,params=channelParams)

def getVideoDetails(videoID):
    api = 'https://youtube.googleapis.com/youtube/v3/videos'
    params = {
        'key': key,
        'part': 'snippet,contentDetails',
        'id': videoID 
    }
    return requests.get(api,params=params)

def checkKeyWords(keywords,text):
    for word in keywords:
        if (word in text):
            return True
    return False
#Finds where the puns end by detecting for certain keywords like shoutouts
def findEnd(videoId):
    keywords = ["school","high school","shout outs","shoutout","shout out","shoutouts","comments"]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(videoId)
    except:
        return 570
    for line in transcript:
        if(line['start'] > 490):
            if(checkKeyWords(keywords,line['text'])):
                return line['start']
    return 570   
            
def verifyEnd(videoId,time):
    driver.get("https://youtu.be/"+videoId+ "?t={}".format(time))
    driver.find_element_by_class_name('ytp-time-current')
    wait()
    end = driver.find_element_by_class_name('ytp-time-current').get_attribute('innerHTML')
    #BAD CODE THAT TURNS YOUTUBE "7:43" format to only seconds
    return int(end[:end.find(':')])*60+int(end[end.find(':')+1:])
    
    
#Gets all of the Videos and Finds the title of each video
#The Youtube API Loads lists of 50 videos at a time, and gives us a pagetoken to go to the next page.
pageToken=""

with open('videos.yaml','r') as f:
    compiledVideos = yaml.load(f,Loader=yaml.FullLoader)
    if(compiledVideos == None):
        compiledVideos = {}
count = 1
#If a break is needed, put the last id number in the starting pos and it'll resume to the starting pos
startingPos = 0
print("To Continue, Press q")
while True:
    rawVideoList = getVideoList(pageToken)
    data = json.loads(rawVideoList.text)
    if(not "nextPageToken" in data):
        break
    pageToken = data["nextPageToken"]
    #Iterates through list of 50 videos
    for video in data["items"]:
        videoId = video["id"]["videoId"]
        title = getVideoDetails(videoId).json()["items"][0]["snippet"]["title"]
        #Manually added these dates when there was an issue while manually verifying.
        omitDates = ["September 11","August 6","August 5","August 4","August 3,","February 3,"]
        if("|" in title and "2020" in title and not checkKeyWords(omitDates,title)):
            if(count<startingPos):
                count+=1
                continue
            #CNN 10 Vidoes are formatted in (Title) | (Date) Format
            date = title[title.find("|")+2:]
            #Uses the youtube transcript API to find an aproximate end.
            end = round(findEnd(videoId))

            #Verify End manually(Optional)
            end = verifyEnd(videoId,end-7)
            #Add Files to Dictionary
            videoValues = {"date":date,"endFrame":end,"videoId":videoId,"id":count}
            compiledVideos[date] = videoValues
            #Save current config to a yaml file
            config = open('videos.yaml','w')
            yaml.dump(compiledVideos,config)
            count+=1
    print(pageToken)

    
    






