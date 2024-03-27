def stutter(word):
    word_to_return = word[:2] + "... " + word[:2] + "... " + word + "?"

    return word_to_return


print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))

