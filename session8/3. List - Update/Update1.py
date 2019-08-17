a = ['sport','lol','bts']
print(*a)
b = input("Enter sth : ")
a.append(b)
print(*a)
a[0] = 'Spiderman'
print(*a, sep=' | ')
