print("Follow the instructions to sign up.")

a = input("Username :")
while True :
    b = input("Email :")
    if "@gmail.com" not in b :
        print("Invalid email \nPlease enter again.")
    elif "@gmail.com" in b :
        break
while True :
    c = input("Password :")
    if c.isalpha() or c.isdigit() or len(c) <= 8 :
        print("Password must have more than 8 characters including both letters and numbers.\nPlease enter a valid password.")
    else :
        print("Vaid password")
        break
while True :    
    d = input("Enter password again :")
    if c != d:
        print("Password incorrect.PLease enter password again.")
    if c == d :
        print("Account successfully registered.")    
        break  