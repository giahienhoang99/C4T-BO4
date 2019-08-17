# Cách 2 : Không dùng hàm sum()

a = [5,1,8,92,-1,30] 
print("Our current num list :",*a, sep=',')
b = 0
for i in range(len(a)) :
    b = b + a[i]
print("Sum of nums :",b)    
