#create a function take in a number ,n , and returns all the prime numbers from 1 to n .
def prime_finder(n):
    lst = []
    for number in range(1, n + 1):
        if number % n == 0:
            lst.append(number)
    return lst



print(prime_finder(11))
