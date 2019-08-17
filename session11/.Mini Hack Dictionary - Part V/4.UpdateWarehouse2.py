laptop_list = {
    "HP"        : 20,
    "DELL"      : 60,
    "MACBOOK"   : 2,
    "ASUS"      : 30,
    "TOSHIBA"   : 10,
    "FUJITSU"   : 15,
    "ALIENWARE" : 5,
}
brand, num = input("Enter a laptop brand to make purchase and number of laptops :").split(':')
total_lapnum = 142
laptops_left = total_lapnum - int(num)
print("Number of laptops left in warehouse :",laptops_left)