profile = {
    "name" : "Bui Minh vu",
    "age" : 15,
    "description" : "tml ",
}
while True : 
    key = input("Enter a key to look up :")
    if key in profile :
        print("Key exists")
    else :
        print("Key does not exist")
