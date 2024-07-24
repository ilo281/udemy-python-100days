def evenly_divisible(a, b, c):
    # 1 generate range from a to b
    my_range = range(a, b + 1)
    # 2  Need to divide each number in the range by c
    # 3 Determine which number from the range can be evenly divide by c
    # 4 Calculate sum of numbers from step 3
    division = 0
    my_sum = 0
    for n in my_range:
        division = n/c
        if n % c == 0:
            my_sum = my_sum+n

    return my_sum


print(evenly_divisible(1, 10, 20))
print(evenly_divisible(1, 10, 2))
print(evenly_divisible(1, 10, 3))

