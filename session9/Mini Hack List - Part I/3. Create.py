a = ["black", "white", "grey"]
print("Our color list :")
print(*a,sep = ",")
b = input("Enter a new color : ")
print("Our new color list :")
a.append(b)
print(*a, sep=',')