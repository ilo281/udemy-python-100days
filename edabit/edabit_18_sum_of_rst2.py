def series_resistance(lst):
    total = 0
    for n in lst:
        total = n + total
    if total <= 1:
        string_to_return = f"{total} ohm"
    else:
        string_to_return = f"{total} ohms"

    return string_to_return


print(series_resistance([1, 5, 6, 3]))
print(series_resistance([16, 3.5, 6]))
print(series_resistance([0.5, 0.5]))
