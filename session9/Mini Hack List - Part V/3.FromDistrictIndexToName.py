dist = ['ST','BĐ','BTL','CG','ĐĐ','HBT']
population = ['150,300','247,100','333,300','266,800','420,900','318,000']
while True :
    for i in range(len(population)) :
        if population[i] == max(population) :
            print("The most crowded district :",*dist[i],sep='')
    break
while True :
    for i in range(len(population)) :
        if population[i] == min(population) :
            print("The least crowded district :",*dist[i],sep='')
    break