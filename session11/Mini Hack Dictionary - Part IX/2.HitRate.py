import random

skill1 = {"Name":"Tackle", "Minimum lv":1, "Damage":5, "Hit rate":0.3 }
skill2 = {"Name":"Quick Attack", "Minimum lv":2, "Damage":3, "Hit rate":0.5 }
skill3 = {"Name":"Strong Kick", "Minimum lv":4, "Damage":9, "Hit rate":0.2 }
skill_list = [skill1,skill2,skill3]

level = 3 
while True :
    print("Light---Lv.3")
    print("Available skills :")
    for i in range(len(skill_list)) :
        print(i+1,".",skill_list[i]["Name"])
    choice = int(input("Use skill number :"))
    if choice == 1 :
        if level < skill1["Minimum lv"] :
            print("Character needs to reach lv.1")
        else :
            r = random.random()
            print(r)
            if r < skill1["Hit rate"]:
                print("Damage caused to opponent :",skill1["Damage"])  
            else :
                print("Missed")    
    elif choice == 2 :
        if level < skill2["Minimum lv"] :
            print("Character needs to reach lv.2")
        else :
            r = random.random()
            print(r)
            if r < skill2["Hit rate"]:
                print("Damage caused to opponent :",skill2["Damage"])  
            else :
                print("Missed")           
    elif choice == 3 :
        if level < skill3["Minimum lv"] :
            print("Character needs to reach lv.4")
        else :
            r = random.random()
            print(r)
            if r < skill3["Hit rate"]:
                print("Damage caused to opponent :",skill3["Damage"])  
            else :
                print("Missed")          
    else :
        print("No skill.Enter again.")          