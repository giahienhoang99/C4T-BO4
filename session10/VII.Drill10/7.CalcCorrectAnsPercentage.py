correct_ans_counter = 0

quest1 = {
    "Q1":"How many legs does an octopus have ?",
    "A1":"1. No legs",
    "A2":"2. 5 legs",
    "A3":"3. 7 legs",
    "A4":"4. 8 legs",
}
 
for k,v in quest1.items() :
    print(k,":",v) 
ans1 = int(input("Enter 1,2,3 or 4 as your choice of answer :"))
if ans1 == 4 :
    print("Correct !!!")
    correct_ans_counter = correct_ans_counter + 1
else :
    print("Wrong !!!")       
    print("The correct answer is #4. 8 legs")

quest2 = {
    "Q1":"How many legs does a spider have ?",
    "A1":"1. No legs",
    "A2":"2. 5 legs",
    "A3":"3. 8 legs",
    "A4":"4. 10 legs",
}
 
for k,v in quest2.items() :
    print(k,":",v) 
ans2 = int(input("Enter 1,2,3 or 4 as your choice of answer :"))
if ans2 == 3 :
    print("Correct !!!")
    correct_ans_counter = correct_ans_counter + 1
else :
    print("Wrong !!!")       
    print("The correct answer is #3. 8 legs")    

quest3 = {
    "Q1":"How many legs does Spiderman have ?",
    "A1":"1. No legs",
    "A2":"2. 2 legs",
    "A3":"3. 3 legs",
    "A4":"4. 5 legs",
}
 
for k,v in quest3.items() :
    print(k,":",v) 
ans3 = int(input("Enter 1,2,3 or 4 as your choice of answer :"))
if ans3 == 2 :
    print("Correct !!!")
    correct_ans_counter = correct_ans_counter + 1
else :
    print("Wrong !!!")       
    print("The correct answer is #2. 2 legs")
p = correct_ans_counter / 3 * 100
print("You have finished the quiz.\nCorrect answer(s) percentage :",round(p,2),"%")
