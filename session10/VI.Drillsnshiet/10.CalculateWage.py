s1 = {"Name":"Huy", "Role":"Waiter", "Hours":12 , "Salary per hour ($)":0.8 } 
s2 = {"Name":"Tung", "Role":"Cook", "Hours":24 , "Salary per hour ($)":1.5 }
s3 = {"Name":"M.Duc", "Role":"Manager", "Hours":20 , "Salary per hour ($)":2 }
s4 = {"Name":"Don", "Role":"Waiter", "Hours":12 , "Salary per hour ($)":0.9 }
s5 = {"Name":"H.Duc", "Role":"Waiter", "Hours":14 , "Salary per hour ($)":0.7 }

salarynshiet = [s1,s2,s3,s4,s5]
for i in range(len(salarynshiet)) :
    salarynshiet[i]["MonthlyWage"] = round(salarynshiet[i]["Hours"] * salarynshiet[i]["Salary per hour ($)"] * 30, 2)
    print(salarynshiet[i])
    