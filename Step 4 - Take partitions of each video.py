from moviepy.editor import VideoFileClip,TextClip,vfx,CompositeVideoClip
import os
import yaml
cwd = os.getcwd()
print(cwd)

def createPartition(index,videoData):
    os.chdir("videos/"+str(index))
    #Get the start and end second from the YAML Config and edit all of the videos into clips that can be concatinated.
    start = videoData['startFrame']
    end = videoData['endFrame']
    print(start,end)
    mp4 = findmp4()
    print(mp4)
    os.chdir(cwd)
    fileLoc = 'videos' + '\\' + str(index) + '\\' + mp4
    video = VideoFileClip(fileLoc).subclip(start-4,end+2).fx(vfx.fadeout,duration=1).fx(vfx.fadein,duration=5)
    # Make the text. Many more options are available.
    txt_clip = ( TextClip(videoData['date'],fontsize=35,color='white',font='Hans Kendrick')
                 .set_position(("center",80))
                 .set_duration(5).fx(vfx.fadeout,duration=1.5).fx(vfx.fadein,duration=3))
    
    result = CompositeVideoClip([video, txt_clip]) # Overlay text on video

    result.write_videofile("partitions\\" + str(index) + ".mp4") # Write the partition into a new partition folder
    os.chdir(cwd)
    video.close()
    txt_clip.close()
    result.close()
    
    
def findmp4():
    files = os.listdir()
    for x in files:
        if x.endswith('.mp4'):
            return x
    

with open('videos.yaml','r') as f:
    compiledVideos = yaml.load(f,Loader=yaml.FullLoader)

#Final Videos Object
videos = []
#Process the Yaml file into a list in order by Date
for x in range(len(compiledVideos)+1):
    videos.append(1)
for x in compiledVideos:
    print(compiledVideos[x]['id'])
    videos[compiledVideos[x]['id']]=compiledVideos[x]
videos.reverse()


for index,x in enumerate(videos):  
    createPartition(index,x)   
