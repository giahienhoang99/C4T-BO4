a = [5, 1, 8, 92, 7, 30]
print("Our current numlist :",a)
listEven = []
for i in range(len(a)) :
    if a[i] % 2 == 0 :
        listEven.append(a[i])
print("All even numbers :",*listEven)
        