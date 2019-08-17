a = input("Enter a list of numbers, seperated by ' ': ").split(' ')
print(a)
b = 0
for i in range(len(a)) :
    b = b + int(a[i])
print("Sum of nums :",b)    
