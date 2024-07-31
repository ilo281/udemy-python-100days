"""
Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the
two smallest integers must equal the square of the largest number to be validated.
"""


def is_triplet(a, b, c):
    compare = False
    # 1 determine two smallest integers
    my_list = [a, b, c]
    sorted_list = sorted(my_list)
    # 2 determine the largest integer
    # 3 determine the square of each smallest integer and sum of both
    first_var_square = sorted_list[0] ** 2
    second_var_square = sorted_list[1] ** 2
    sum_small_integers = first_var_square + second_var_square
    # 4 determine the square of largest integer
    largest_var_square = sorted_list[2] ** 2

    # 5 compare # 3 and # 4 then return True if they are the same .
    if sum_small_integers == largest_var_square:
        compare = True

    return compare


print(is_triplet(5, 4, 3))

print(is_triplet(13, 5, 12))

print(is_triplet(1, 2, 3))

