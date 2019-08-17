n = int(input("Enter a number : "))

if n % 2 != 0 :
    range1 = range(n, 0, -2)
    print(*range1)
else : 
    range1 = range(n-1, 0, -2)
    print(*range1)

