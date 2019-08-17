print("Follow the instructions to sign up.")

a = input("Username :")
b = input("Email :")
while True :
    c1 = input("Password :")
    c2 = input("Enter password again :")
    if c1 != c2 :
        print("Password incorrect.PLease enter password again.")
    if c1 == c2 :
        print("Account successfully registered.")    
        break
 