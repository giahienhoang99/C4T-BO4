a = ['Spiderman','lol','Dragon Ball']
while True :
    i = int(input("Enter index : "))
    if i < -3 or i > 2 :
        print("Invalid index number. Please enter again.")
    else :
        break    
a.pop(i)
print("New list : ", *a, sep=' | ')
