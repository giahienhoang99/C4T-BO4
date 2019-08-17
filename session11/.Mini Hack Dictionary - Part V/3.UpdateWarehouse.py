laptop_list = {
    "HP"        : 20,
    "DELL"      : 60,
    "MACBOOK"   : 2,
    "ASUS"      : 30,
    "TOSHIBA"   : 10,
    "FUJITSU"   : 15,
    "ALIENWARE" : 5,
}
a = input("Enter a laptop brand to make purchase :")
num = int(input("Enter the number of laptops you want :"))
total_lapnum = 142
laptops_left = total_lapnum - num 
print("Number of laptops left in warehouse :",laptops_left)