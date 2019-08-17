while True :
    a = ['sao','charlotte','slime']
    b = input("Choose one C or R or U or D : ")
    if b == "C" :
        c = input("Enter sth you like : ")
        a.append(c)
        print(*a)
    if b == "R" :
        l = len(a)
        if l > 0 :
            for i in range(l) :
                print(*a[i], sep = " ")
        if l == 0 :
            print("List includes nothing.")
    if b == "U" :
        while True :
            i = int(input("Enter index : "))
            if i < -3 or i > 2 :
                print("Invalid index number")
            else :
                break 
        r = input("Enter sth you would like to update/replace : ")
        a[i] = r
        print(*a)
    if b == "D" :
        while True :
            i = int(input("Enter index : "))
            if i < -3 or i > 2 :
                print("Invalid index number.")
            else :
                break
        a.pop(i)
        print(*a)

     





    