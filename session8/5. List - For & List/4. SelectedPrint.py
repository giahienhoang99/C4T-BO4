a = ['Spiderman','lol','Dragon Ball','Charlotte','sao','naruto']
l = len(a)
for i in range(l) :
    if "e" in a[i] or "E" in a[i] :
        print(*a[i].upper(), sep="")