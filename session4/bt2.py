while True : 
    a = input("Please enter your password : ")
    if a.isalpha() :
        print("Valid")
        break
    else : 
        print("Invalid.Try again.")
