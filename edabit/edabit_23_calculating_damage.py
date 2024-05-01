def damage(damage, speed, time):
    amount_of_damage = 0
    if time == "second":
        amount_of_damage = damage * speed
    if time == "minute":
        amount_of_damage = (damage * speed) * 60
    if time == "hour":
        amount_of_damage = ((damage * speed) * 60) * 60
    if damage < 0 :
        amount_of_damage = "invalid"
    if speed < 0:
        amount_of_damage = "invalid"

    return amount_of_damage


print(damage(40, 5, "second"))
print(damage(100, 1, "minute"))
print(damage(2, 100, "hour"))
print(damage(-40, -5, "second"))
print(damage(40, -5, "second"))
print(damage(-40, 5, "second"))
