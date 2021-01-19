# CNN 10 Carl Azuz puns editor
> Hello! Thanks for checking out this repo. **This project consists of a set of 5 scripts which have the purpose of getting, downloading, editing, and eventually putting together a compillation video.** These scripts are designed for a student news show called CNN 10 which is hosted by Carl Azuz. Carl Azuz is famous for the "10 out of 10" sequence of his show, where he talks about something prevelent/intresting in popular culture or media and then also proceeds to make puns about said topic. 

> I wanted to make a compilation video of all these puns together and saw that the editing in making this video would be quite repetitive, and something that could be scriptable. The editing, downloading, and parsing together of the video wouldn't be hard, but as I'll explain later, the hardest part came with editing the video and knowing where he starts and ends his puns.

## All Dependencies (In order of apperance)
- Selenium (Manual verification of End Frame)
- YAML (Video Config)
- Youtube Trasncript API (Aproximate verification of End Frame)
- Keyboard (Hotkey)
- PyTube (Download Videos)
- PyTesseract(OCR)
- CV2 (Video Splicing and Image Processing)
- MoviePy (Editing)

### **Step 1**
This script accesses the youtube API and gets a video list of the CNN 10 channel. It then goes through that list and finds all main CNN10 Episodes from 2020. After a episode is found, it will attempt to find the aproximate end of puns through the Youtube Transcript API. It looks for keywords like "shout-out" or "high school" because when he starts shouting out schools, it almost always indicates the puns are done. 

This endframe is then manually checked by loading the video using selenium. The user will then pause the video where it actually ends and press a hotkey to go onto the next video. Selenium will then take the html element of the timer and all of the data is saved into a YAML Config. Repeat for all videos. Each video is also given an ID for an easier way to denote chronological order.

*This step requires the chrome driver and a key.txt of your youtube API key.*

### **Step 2**
Takes the Video ID from the YAML Config and downloads all the videos into a folder called 'videos', with each video given its own folder.

### **Step 3**
Each video has their last half spliced into many images, and searched for the keywords "10 out of 10". This denotes the beginning of the puns sequence, and this start frame is saved into the config.

### **Step 4**
Using the now complete config, each video is edited with a fade in and fade out and the start and end positions, and also an acompanying Date Text field to introduce the clip. These are saved into a folder called partitions.

### **Step 5**
All the clips are then finally parsed together, done in parts due to a lack of memory and power on my machine.


## Optimizations
Some of these parts could be streamlined a bit easier. The splicing of all the frames is quite unnecssary, as an image could be directly inputted into OCR in python. I also should've used the Python Youtube API libary, for a bit of abstraction.

## Final Product
[![CNN 10 Puns 2020](http://img.youtube.com/vi/9jJxPQm7QIA/0.jpg)](https://youtu.be/9jJxPQm7QIA "CNN 10 Puns 2020")