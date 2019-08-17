quest = {
    "Q1":"How many legs does an octopus have ?",
    "A1":"1. No legs",
    "A2":"2. 5 legs",
    "A3":"3. 7 legs",
    "A4":"4. 8 legs",
}
 
for k,v in quest.items() :
    print(k,":",v) 
ans = int(input("Enter 1,2,3 or 4 as your choice of answer :"))