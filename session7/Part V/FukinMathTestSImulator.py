from random import *
while True:
    x = randint(1,100)
    y = randint(1,100)
    z = randint(-1,1)
    sum = x+y+z
    print(x,"+",y,"=",sum)
    ans = input("D/S:").lower()
    if z == 0:
        if ans == "d" or "D":
            print("Dung roi ^^")
        elif ans == "s" or "S":
            print("Sai roi :((")
            break
        else:
            print("Nhap lai nhe")
    else:
        if ans == "d" or "D":
            print("Sai roi :((")
            break
        elif ans == "s" or "S":
            print("Dung roi ^^")
        else:
            print("Nhap lai nhe")