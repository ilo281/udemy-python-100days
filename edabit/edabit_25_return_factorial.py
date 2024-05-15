def factorial(num):
    num_factorial = 1

    for i in reversed(range(1, num+1)):
        num_factorial = num_factorial * i

    return num_factorial


print(factorial(3))
print(factorial(5))
print(factorial(13))
