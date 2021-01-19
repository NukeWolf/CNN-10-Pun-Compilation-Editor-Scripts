from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
clips = []
conc = []
os.chdir("partitions")

#Concat sets of 10 videos together and then will parse together those sets of videos together
#This is due to a lack of memory. Parseing 195 videos at once doesn't work.
for index in range(193):
    if index<193:
        clips.append(VideoFileClip(str(index)+".mp4"))
    if (index % 10 == 9):
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(str(index)+"conc.mp4")
        conc.append(str(index)+"conc.mp4")
        final_clip.close()
        for c in clips:
            c.close()
        clips = []
final_clip = concatenate_videoclips(clips)
final_clip.write_videofile("finalconc.mp4")
conc.append("finalconc.mp4")
final_clip.close()
for c in clips:
    c.close()
clips = []

for c in conc:
    clips.append(VideoFileClip(c))
final_clip = concatenate_videoclips(clips)
final_clip.write_videofile("Final.mp4")
final_clip.close()