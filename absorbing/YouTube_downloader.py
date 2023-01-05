
import progressbar as progress
from pytube import YouTube
from os import system
from colorama import Fore

def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = ys.filesize
    size = contentsize - bytes_remaining

    print(Fore.CYAN,'\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')


while True:
    system("cls")
    print(Fore.LIGHTBLUE_EX,"welcome to youtube downloader")
    url = input("enter youtube URL (type 'exit' to quit): ")
    
    if url == 'exit':
        break

    yt = YouTube(url)
    print(f"{Fore.LIGHTYELLOW_EX}Title: {yt.title} {Fore.RESET}")
    var = input(f"{Fore.LIGHTGREEN_EX}you want 'audio' or 'video' (type 'exit' to quit)?: {Fore.RESET}")

    if var == 'audio':
        ys = yt.streams.get_audio_only()
        yt = YouTube(url, on_progress_callback=progress)

    elif var == 'video':
        yt = YouTube(url, on_progress_callback=progress)  
        ys = yt.streams.get_highest_resolution()

    elif var == 'exit':
        break

    else:
        raise ValueError("I couldn't understand. try again!")

    print(Fore.LIGHTGREEN_EX,"***download started***")
    ys.download()
    print("***download finished***")

