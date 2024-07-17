import datetime
def time_for_milk_and_cookies(date):
    year_month_day = date.strftime(('%Y-%m-%d'))  # converting date to string
    month_day = year_month_day[5:]  # slicing to remove first five characters
    milkandcookies = False
    if month_day == "12-24":  # evaluate if month_day is equal 12-24
        milkandcookies = True

    return milkandcookies


print(time_for_milk_and_cookies(datetime.date(2013, 12, 24)))
print(time_for_milk_and_cookies(datetime.date(2013, 1, 23)))
print(time_for_milk_and_cookies(datetime.date(3000, 12, 24)))
print(time_for_milk_and_cookies(datetime.date(2023, 12, 24)))
print(time_for_milk_and_cookies(datetime.date(4000, 12, 11)))
