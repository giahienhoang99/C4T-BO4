highscores = ['45','67','56','78']
for i,score in enumerate(highscores) :
    print(i+1,".", *highscores[i],sep='')
