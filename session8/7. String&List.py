fav = str(input("Name your things : ")).split(',')
l = len(fav)
print("Your things :")
for i in range(l) :
    print(*fav[i], sep = '')
