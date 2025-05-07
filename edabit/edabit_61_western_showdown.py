# create function that take  two strings and return a string
# use split function to split first argument on Bang!
# use len function to determine length of empty spaces at the beginnig
# use split function to split second argument on Bang!
# use len function to determine length of empty spaces at the beginnig
# compare length between two
def showdown(p1, p2):
    winner = ""
    p1_split = p1.split("Bang!")
    empty_space_p1 = len(p1_split[0])
    p2_split = p2.split("Bang!")
    empty_space_p2 = len(p2_split[0])
    if empty_space_p2 > empty_space_p1:
        winner = "p1"
    if empty_space_p2 < empty_space_p1:
        winner = "p2"
    if empty_space_p2 == empty_space_p1:
        winner = "tie"

    return winner


print(showdown(
  "   Bang!        ",
  "        Bang!   "))
print(showdown(
  "               Bang! ",
  "             Bang!   "))

print(showdown(
  "     Bang!   ",
  "     Bang!   "
))
