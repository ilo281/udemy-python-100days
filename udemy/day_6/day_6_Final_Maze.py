def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_on_right() and front_is_clear():
        move()
    if not wall_on_right() and not front_is_clear():
        turn_right()
    else:
        if not at_goal():
            turn_left()