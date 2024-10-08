#non eseguire su SSH

import os
import shutil
import yt_dlp

YDL_OPTIONS_AUDIO={'format':'bestaudio','outtmpl':'/temp_a/%(title)s.mp3'}
YDL_OPTIONS_VIDEO={'format':'bestvideo','outtmpl':'/temp_v/%(title)s.mp4'}

if os.path.isfile('directory.txt') == False:
    x=open("directory.txt","x")
if os.path.isfile('temp_a') == False:
    os.mkdir('temp_a')
    os.mkdir('temp_v')

link=input("Paste the YouTube Link or type chdir: ")

if link == "chdir":
    directory=input("Choose the new directory: ")
    x=open("directory.txt","w")
    x.write(directory)
    x.close()
    link=input("Paste the YouTube Link: ")
    
def download():
    type=input("1)Video 2)Audio :")
    
    x=open("directory.txt","r")
    directory=x.read()
    if directory == "":
        directory=input("Choose a directory: ")
        if directory != "":
            save_directory=input("Save this directory [y] or [n]: ")
            if save_directory == "y":
                f =open("directory.txt","a")
                f.write(directory)
                f.close()
    x.close()

    if int(type) == 1:
    
        yt_dlp.YoutubeDL(YDL_OPTIONS_VIDEO).download(f'{link}')
        os.chdir(os.getcwd()+'/temp_v')
        dir=os.listdir()
        shutil.move(dir[0],directory)
    
    if int(type) == 2:
    
        yt_dlp.YoutubeDL(YDL_OPTIONS_AUDIO).download(f'{link}')
        os.chdir(os.getcwd()+'/temp_a')
        dir=os.listdir()
        shutil.move(dir[0],directory)
    
if link.startswith(("https://youtu.be","https://www.youtube.com")):
    download()
else :
    print("Provide a valid YouTube link")

