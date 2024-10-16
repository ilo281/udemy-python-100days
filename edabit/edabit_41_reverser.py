def reverse(input_string):
    # 1 reverse input string
    reversed_string = ""
    reversed_string = input_string[::-1]

    # 2 return reversed string  with opposite case
    opposite_case = reversed_string.swapcase()

    return opposite_case


print(reverse("Hello World"))
print(reverse("ReVeRsE"))
print(reverse("Radar"))
