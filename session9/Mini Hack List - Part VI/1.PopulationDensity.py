population = [150.300, 247.100, 333.300, 266.800, 420.900, 318.000]
area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
density = []
while True :
    for i in range(len(area)) :
        density.append(round(population[i] / area[i], 2))
    break
print("Population density : ", density)    