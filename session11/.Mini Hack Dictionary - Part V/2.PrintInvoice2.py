laptop_list = {
    "HP": 600,

    "DELL": 650,

    "MACBOOK": 12000,

    "ASUS": 400,

    "ACER": 350,

    "TOSHIBA": 600,

    "FUJITSU": 900,

     "ALIENWARE": 1000,
}
a = input("Enter a laptop brand to make purchase :")
num = int(input("Enter the number of laptops you want :"))
receipt = laptop_list[a.upper()] * num
print("Receipt :", receipt)