def mood_today(mood=""):
    sentence = ""
    if mood == "happy":
        sentence = f"Today, I am feeling {mood}"
    if mood == "sad":
        sentence = f"Today, I am feeling {mood}"
    if mood == "":
        sentence = "Today, I am feeling neutral"
    return sentence


print(mood_today("happy"))
print(mood_today("sad"))
print(mood_today())