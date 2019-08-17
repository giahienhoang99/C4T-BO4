import random
a = list(input("Enter sth : "))
random.shuffle(a)
print(*a)
l = len(a)
for i in range(l) :
    print(*a[i])