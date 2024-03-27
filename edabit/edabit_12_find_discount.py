def dis(price, discount):
    sale = price / 100 * discount

    newp = price - sale

    return str(round(newp, 2))


print(dis(1500, 50))
print(dis(89, 20))
print(dis(100, 75))
