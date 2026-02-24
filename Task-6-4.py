from robot import *

for i in range(5):
    for j in range(5):
        if is_wall_down() and i > 0:
            paint()
        if i % 2 == 0 and is_free_right():
            move_right()
        elif is_free_left():
            move_left()
    if is_free_up():
        move_up()