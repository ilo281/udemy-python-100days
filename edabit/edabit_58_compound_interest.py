# 1 Create a function that accepts the principal p, the term in years t, the interest rate r, and the number of
# compounding periods per year n .
# 2 The function returns the value at the end of term rounded to the nearest cent.
# 3 Create a formula to calculate compound interest
def compound_interest(p, t, r, n):
    compound_interest_to_return = p * (1 + (r / n)) ** (n*t)
    round_two_interest = round(compound_interest_to_return, 2)

    return round_two_interest


print(compound_interest(10000, 10, 0.06, 12))
print(compound_interest(100, 1, 0.05, 1))
print(compound_interest(3500, 15, 0.1, 4))
print(compound_interest(100000, 20, 0.15, 365))
