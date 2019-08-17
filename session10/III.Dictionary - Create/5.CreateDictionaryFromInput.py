a = {}

while True :
    b = input("Enter a key :")
    c = input("Enter a value :")
    a[b] = c
    if len(a) == 3 :
        break
while True :
    print(a)
    for key, value in a.items() :
        print(key, '.', value)
    break

