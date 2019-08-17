a = ['black','white','grey','blue']
print("Our current color list :",*a,sep=",")
x = input("nhap so hay chu ?")
if x.isdigit():
    a.pop(int(x))
    print("Our new color list :")
    for i,color in enumerate(a) :
        print(i+1,".", *a[i], sep='')
else: 
    a.remove(x)
    print("Our new color list :")
    for i,color in enumerate(a) :
        print(i+1,".", *a[i], sep='')
    