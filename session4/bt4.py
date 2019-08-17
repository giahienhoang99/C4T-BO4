num = 124
count = 0
while True: 
    num = num // 10
    count += 1
    if(num == 0):
        print(count)
        break