def calculator(num1, operator, num2):
    calc = 0
    if operator == "+":
        calc = num1 + num2
    if operator == "*":
        calc = num1 * num2
    if operator == "/":
        if num2 == 0:
            calc = "Can't divide by 0!"
        if num2 != 0:
            calc = num1 / num2
            calc = int(calc)

    return calc


print(calculator(2, "+", 2))
print(calculator(2, "*", 2))
print(calculator(4, "/", 2))
print(calculator(4, "/", 0))
