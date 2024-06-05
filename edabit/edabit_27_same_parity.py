def parity_analysis(num):
    parity = False
    this_sum = 0
    for i in str(num):
        this_sum = this_sum + int(i)
    if this_sum % 2 == 0 and num % 2 == 0:
        parity = True
    if this_sum % 2 != 0 and num % 2 != 0:
        parity = True
    return parity


print(parity_analysis(243))

print(parity_analysis(12))

print(parity_analysis(3))
