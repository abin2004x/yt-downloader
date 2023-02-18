import subprocess
from datetime import date

try:
    from pytube import YouTube,Playlist
except:
    subprocess.call(['pip3', 'install', "pytube"])
    from pytube import YouTube,Playlist
    print("Requred packages are successfully installed.\n")


def video_download(url,output_path):
    YouTube(url).streams.get_highest_resolution().download(output_path,filename=YouTube(url).title.replace("|","") + ".mp4")
    print(YouTube(url).title.replace("|","") + ".mp4", "downloaded successfully.")

def audio_download(url,output_path):
    YouTube(url).streams.get_audio_only().download(output_path,filename=YouTube(url).title.replace("|","") + ".mp3")
    print(YouTube(url).title.replace("|","") + ".mp3", "downloaded successfully.")

def video_checkig(url):
    v_or_a=input("video or audio (v,a):")
    output_path="/home/nightcoder/Downloads/"+str(date.today())+"/"
    if v_or_a == "v":
        video_download(url,output_path)
    elif v_or_a == "a":
        audio_download(url,output_path)
    elif v_or_a == "b":
        audio_download(url,output_path)
        video_download(url,output_path)
    else:
        print("enter a valid input.")
        video_checkig(url)

def playlist_checkig(url):
    v_or_a=input("Select video or audio to be  (v,a):")
    output_path="/home/nightcoder/Downloads/"+Playlist(url).title+"/"
    if v_or_a == "v":
        for url in Playlist(url).video_urls:
            video_download(url,output_path)
    elif v_or_a == "a":
        for url in Playlist(url).video_urls:
            audio_download(url,output_path)
    elif v_or_a == "b":
        for url in Playlist(url).video_urls:
            audio_download(url,output_path)
            video_download(url,output_path)
    else:
        print("enter a valid input.")
        video_checkig(url)

def video_playlist(url):
    print('Number Of Videos In playlist: %s' % len(Playlist(url).video_urls))
    playlist_checkig(url)

url=input("Enter a yt link:")
if "playlist?" in url:
    video_playlist(url)
else:
    video_checkig(url)