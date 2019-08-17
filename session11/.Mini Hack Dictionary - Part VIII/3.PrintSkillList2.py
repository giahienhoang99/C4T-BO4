skill1 = {"Name":"Tackle", "Minimum lv":1, "Damage":5, "Hit rate":0.3 }
skill2 = {"Name":"Quick Attack", "Minimum lv":2, "Damage":3, "Hit rate":0.5 }
skill3 = {"Name":"Strong Kick", "Minimum lv":4, "Damage":9, "Hit rate":0.2 }
skill_list = [skill1,skill2,skill3]

print("Character's skills :")
for i in range(len(skill_list)) :
    print(i+1,".",skill_list[i]["Name"])