def end_corona(recovers, new_cases, active_cases):
    numbers_days = active_cases / (recovers - new_cases)

    return numbers_days


print(end_corona(4000, 2000, 77000))
print(end_corona(3000, 2000, 50699))
print(end_corona(30000, 25000, 390205))
