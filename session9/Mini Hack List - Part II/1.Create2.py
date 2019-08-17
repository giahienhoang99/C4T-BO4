a = ["black", "white", "grey"]
b = int(input("Enter position : "))
print("Color at position %s :" %(b))
print(*a[b], sep="")
