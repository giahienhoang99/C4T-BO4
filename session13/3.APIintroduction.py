
import json

with open("userdata.json") as userdata :
    dataGet = json.load(userdata)

for i in range(len(dataGet)) :
    if "Delphine" in dataGet[i]['username'] :
        print("Username :")
        print(dataGet[i]["username"])


