def next_edge(side1, side2):
    third_edge = (side1 + side2) - 1

    return third_edge


print(next_edge(8, 10))
print(next_edge(5, 7))
print(next_edge(9, 2))
