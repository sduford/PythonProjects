import math


def areaofcone(radius, height):

    area = math.pi * radius(radius + math.sqrt((height**2 + radius**2)))
    return area

print(areaofcone(1.5,3))
