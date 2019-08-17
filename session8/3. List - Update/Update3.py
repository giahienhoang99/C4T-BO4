a = ['Spiderman','lol','Dragon Ball']
print(a)
while True :   
    i = int(input("Enter index : "))
    if i < -3 or i > 2 :
        print("Invalid index number. Please enter again. ")
    else :
        break 
b = input("Enter sth to replace : ")
a[i] = b
print(*a, sep=' | ')
