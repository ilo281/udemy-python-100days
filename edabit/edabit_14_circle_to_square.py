from math import pi, sqrt


def circle_or_square(radius, area):
    circumference = 2 * pi * radius
    perimetr = sqrt(area)*4
    circle1 = None
    if circumference > perimetr:
        circle1 = True
    if circumference < perimetr:
        circle1 = False

    return circle1


print(circle_or_square(16, 625))
print(circle_or_square(5, 100))
print(circle_or_square(8, 144))
