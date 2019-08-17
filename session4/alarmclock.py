from datetime import datetime
currentTime = datetime.now().strftime('%H:%M')

import pyglet
music = pyglet.resource.media("crowd-cheering.mp3")
 
print("It is currently ", currentTime)
while True :
    alarmTime = input("Alarm at : ")
    if currentTime == alarmTime :
        print("It is time to wake up !")
        music.play()
        pyglet.app.run()
        break
    else :
        print("Alarm set")
        break
        