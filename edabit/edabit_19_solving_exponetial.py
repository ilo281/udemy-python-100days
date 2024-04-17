def solve_for_exp(a, b):
    missing_exponent = 1
    while missing_exponent <= 9:
        total = a ** missing_exponent
        if total == b:
            break
        missing_exponent += 1
    return missing_exponent


print(solve_for_exp(4, 1024))
