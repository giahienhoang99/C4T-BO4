a = input("Enter a list of numbers seperated by ' ':").split(' ')
print("Your current numlist :")
print(*a,sep=',')
listEven = []
for i in range(len(list(a))) :
    if int(a[i]) % 2 == 0 :
        listEven.append(a[i])
print("All even numbers from entered list :")
print(*listEven,sep=',')
