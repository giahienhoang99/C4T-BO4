a = ["5","1","8","92","-1","30"]
while True :
    num = input("Enter a number : ")
    if num in a :
        for i in range(len(a)):
            if a[i] == num:
                print("Found, position", i + 1)
        break
    else: 
        print("not in list or not an interger")