from turtle import *

numofsides = int(input("Enter number of sides: "))
length = int(input("Enter length of sides: "))
Angle = 360 / numofsides

for i in range(numofsides):
    forward(length)
    right(Angle)

mainloop()
