laptop_list = {
    "HP" : 20,

    "DELL" : 50,

    "MACBOOK" : 12,

    "ASUS" : 30,
}
newlap = input("Enter a new laptop brand :")
num = int(input("Enter the number of laptops :"))
laptop_list[newlap.upper()] = num
print(laptop_list)