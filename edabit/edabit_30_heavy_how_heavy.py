import math


def weight(r, h):
    volume = math.pi*r**2*h
    mass = (1 / 1000)*volume

    return round(mass, 2)


print(weight(4, 10))
print (weight(30, 60))
print(weight(15, 10))
