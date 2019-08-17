while True : 
    a = input("password : ")
    if len(a) <=8 :
        print("password needs to have more than 8 characters")
    elif a.isalpha() :
        print("password needs to include letters and numbers")
    elif a.isdigit() :
        print("password needs to include letters and numbers")   
    else : 
        print("valid password")
        break
