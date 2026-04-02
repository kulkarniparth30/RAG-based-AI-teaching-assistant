# convert videos to mp3

import os 
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')

files = os.listdir("videos")

for file in files:
    #print(file.encode('utf-8', errors='ignore').decode())
    
    tutorial_number = file.split(" [")[0].split(" #")[1]
    file_name = file.split(" ｜ ")[0]
    print(tutorial_number , file_name)
    subprocess.run(["ffmpeg", "-i" ,  f"videos/{file}" , f"audios1/{tutorial_number}_{file_name}.mp3"])