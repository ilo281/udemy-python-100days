import math
def number_split(n):
    left_half = n / 2
    right_half = n - left_half
    if left_half % 2 != 0:
        left_half = math.floor(left_half)
    if right_half % 2 != 0:
        right_half = math.ceil(right_half)

    list_to_return = [int(left_half), int(right_half)]

    return list_to_return


print(number_split(4))
print(number_split(10))
print(number_split(11))
print(number_split(-9))
