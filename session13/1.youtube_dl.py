from __future__ import unicode_literals
import json
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])   
    ydl.download(['https://www.youtube.com/watch?v=n6BwAWiHcSg&t=182s']) 

dataGet = youtube_dl.YoutubeDL(ydl_opts).extract_info('https://www.youtube.com/watch?v=BaW_jenozKc', False)
print(dataGet)

with open("data.json", "w") as outFile:
    json.dump(dataGet, outFile) 
