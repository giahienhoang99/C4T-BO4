a = ['Spiderman','lol','Dragon Ball','Charlotte','sao','naruto']
for i,item in enumerate(a) :
    print(i+1,'.', *a[i].upper())
    