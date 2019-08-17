from __future__ import unicode_literals
import youtube_dl
from pyglet.media import Source, Player, load
import json

while True:
    print("""
This is a app music
Choose these option behind

1. Show all song
2. Show detail song
3. Play a song
4. Search and download a song
5. Exit

Pick 1 option
    """)

    choose = int(input(">>> "))

    if choose == 4 :
        with open("dataSong.json") as outFile:
            dataGet = json.load(outFile)

        print(dataGet)

        keyWordDownload = input('Enter a song you want to search ')
        ydl_opts = {
            "default_search": "ytsearch3"
        }
        
        searchResult = youtube_dl.YoutubeDL(ydl_opts).extract_info(keyWordDownload, False)

        for i in range(len(searchResult['entries'])):
            print(i + 1, ".", searchResult['entries'][i]['title'])
        
        print("Enter a number you want to download")

        chooseSongDownload = int(input(">>> ")) - 1

        optsDownload = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio', # Tách lấy audio
                'preferredcodec': 'mp3',  # Format ưu tiên là mp3
                'preferredquality': '192', # Chất lượng bitrate
            }],
        }

        songDownload =  youtube_dl.YoutubeDL(optsDownload).extract_info(searchResult['entries'][chooseSongDownload]['webpage_url'], True)

        dataGet.append(songDownload)

        with open("dataSong.json", "w") as dumpData:
            json.dump(dataGet, dumpData)


    elif choose == 3:
        with open("dataSong.json") as outFile:
            dataGet = json.load(outFile)
        
        for i in range(len(dataGet)):
            print(i + 1, ".", dataGet[i]['title'])
        
        print("Choose a song to play")
        chooseSongPlay = int(input(">>> ")) - 1
        songName = dataGet[chooseSongPlay]['title'] + '-' + dataGet[chooseSongPlay]['id'] + ".mp3"
        player = Player()
        source = load(songName)
        player.queue(source)
        player.play()
        while True:
            input('Press any key to exit')
            break