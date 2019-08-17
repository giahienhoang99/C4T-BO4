highscores = ['45','67','56','78']
for i,score in enumerate(highscores) :
    highscores.sort(reverse = True)
    print(i+1,".", *highscores[i],sep='')
while True :
    new_hscore = input("Enter your new highscore : ")
    highscores.append(new_hscore)
    highscores.sort(reverse = True)
    for i,score in enumerate(highscores) :
        if i < 5 :
            print(i+1,".", *highscores[i],sep='')