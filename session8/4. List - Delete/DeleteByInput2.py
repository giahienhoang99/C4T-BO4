a = ['Spiderman','lol','Dragon Ball']
print("Existing list : ", *a, sep=' | ')
while True :
    i = input("Enter variable to delete : ")
    if i not in a :
        print("String not found. Please enter again.")
    else :
        break    
a.remove(i)
print("New list : ", *a, sep=' | ')
