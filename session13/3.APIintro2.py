import json

with open("userdata.json") as userdata :
    dataGet = json.load(userdata)

a = input("Enter username :").capitalize()
print(a)

for i in range(len(dataGet)) :
    if a == dataGet[i]['username'] :
        print("User's ID :", dataGet[i]["id"]) 
