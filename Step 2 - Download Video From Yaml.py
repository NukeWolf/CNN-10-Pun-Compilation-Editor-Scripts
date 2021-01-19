import yaml
from pytube import YouTube

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
#IDs go from most recent video to oldest video. We reverse so we start in january.
videos.reverse()


def downloadVideo(videoId,path):
    link="https://www.youtube.com/watch?v="+videoId
    try:  
        # object creation using YouTube 
        # which was imported in the beginning  
        yt = YouTube(link)
        print
    except:  
        print("Connection Error") #to handle exception  
  
    # filters out all the files with "mp4" extension  
    #mp4files = yt.streams.filter('mp4')  

    # get the video with the extension and 
    # resolution passed in the get() function
    d_video = yt.streams.get_highest_resolution()
    print('Downloading: '+link)
    # downloading the video  
    print(d_video)
    d_video.download(path)  
    
    print('Task Completed!')  

for index,x in enumerate(videos):
    downloadVideo(x['videoId'],"videos/"+str(index))
    