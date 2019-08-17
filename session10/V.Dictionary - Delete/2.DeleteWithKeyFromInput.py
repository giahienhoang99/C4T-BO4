profile = {
    "name" : "Bui Minh vu",
    "age" : 15,
    "description" : "tml ",
}
print("Current profile :", profile)
while True :
    a = input("Choose key to delete :")
    if a not in profile :
        print("Key not found or does not exist.Please re-enter.")
    else :
        break

del profile[a]
print("Updated profile :", profile)         