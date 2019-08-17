# import pyglet
# music = pyglet.resource.media("crowd-cheering.mp3")
# music.play()
# pyglet.app.run()


from pyglet.media import Source, Player, load
import pyglet

player = Player()
source = load('crowd-cheering.mp3')
player.queue(source)
player.play()
pyglet.app.run()
while True:
  input('Press any key to exit')
  break