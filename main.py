from src.functions import listas
from src.streaming import playbackrandom, playback
from src.downloader import downloadtiktoks
from src.byuser import streamuser, getLinks
import sys, os, subprocess


try:
    question = int(input("""Welcome to CLI TikTok, an open-source TikTok viewer!
        
        Do you want to download or watch tiktoks?
        
        (1) Download
        (2) Watch
        """))
    os.system("cls || clear")
    ## DOWNLOAD
    if question == 1:
        downloadquestion = int(input("""Do you want to download your liked videos or a creator?
        
        (1) Liked Videos
        (2) Creator
        """))
        os.system("cls || clear")
        if downloadquestion == 1:
            urls = listas()[0]
            downloadtiktoks(urls)
            sys.exit()
        if downloadquestion == 2:
            print('Due to specific limitations of the current data method, downloading by creator will only get the latest 30 videos.')
            print('This limitation is being actively researched, any contributions will be welcome.')
            username = str(input('Enter the tiktok username here: '))
            links = getLinks(username)
            downloadtiktoks(links)
            sys.exit()
        
    ## STREAM
    if question == 2:
        
        watchquestion = int(input("""Do you want to watch your liked videos or a creator?
        
        (1) Liked Videos
        (2) Creator
        """))
        os.system("cls || clear")
        if watchquestion == 1:
            
            #Liked videos random?
            randomquestion = int(input("""Do you want to watch the tiktoks in randomized order?
            (1) Yes
            (2) No                                       
        """))
            os.system("cls || clear")
            if randomquestion == 1:
                urls = listas()[0]
                datas = listas()[1]
                playbackrandom(urls, datas)
                sys.exit()
            if randomquestion == 2:
                urls = listas()[0]
                datas = listas()[1]
                playback(urls, datas)
                sys.exit()
        
        if watchquestion == 2:
            print('Due to specific limitations of the current data method, watching by creator will only get the latest 30 videos.')
            print('This limitation is being actively researched, any contributions will be welcome.')
            username = str(input('Enter the tiktok username here: '))
            streamuser(username)
            sys.exit()
            
    print("The option you chose isn't valid.")
except ValueError:
    print("The option you chose isn't valid.")
except FileNotFoundError:
    print("The 'Likes.txt' file was not found. Make sure it is in the program folder and try again.")
except subprocess.CalledProcessError:
    os.system("cls || clear")
    print("Mpv media player was not found on your system path. Make sure it's installed and try again.")
except KeyboardInterrupt:
    print("\tKeyboardInterrupt was detected - Goodbye!")