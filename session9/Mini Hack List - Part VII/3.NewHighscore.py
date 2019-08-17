highscores = ['45','67','56','78']
for i,score in enumerate(highscores) :
    print(i+1,".", *highscores[i],sep='')
new_hscore = input("Enter your new highscore : ")
highscores.append(new_hscore)
for i,score in enumerate(highscores) :
    print(i+1,".", *highscores[i],sep='')