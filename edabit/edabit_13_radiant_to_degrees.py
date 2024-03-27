from math import pi

def radians_to_degrees(rad):
    convert = rad * 180 / pi

    return str(round(convert, 1))


print(radians_to_degrees(1))
print(radians_to_degrees(20))
print(radians_to_degrees(50))
