import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "INIT":

        if True:
            state = "right"
            t.setheading(0)  # Разворот вправо
            return state, turn

        # return state, turn
    
    if state == "right":
        t.forward(10*turn)  # Перемещение

        if x >= turn:
            state = "up"
            t.setheading(90)  # Разворот вверх
            return state, turn
        if turn >= num_turns:
            state = "stop"
            return state, turn
        return state, turn
    if state == "up":
        t.forward(10*turn)  # Перемещение

        if y >= turn:
            state = "left"
            t.setheading(180)  # Разворот влево
            return state, turn
        return state, turn
    if state == "left":
        t.forward(10*turn)  # Перемещение

        if x <= -turn:
            state = "down"
            t.setheading(270)  # Разворот вниз
            return state, turn
        return state, turn
    if state == "down":
        t.forward(10*turn)  # Перемещение

        if y <= -turn:
            state = "right"
            t.setheading(0)  # Разворот вправо
            turn += 1
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "INIT"
    end_state = "stop"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if __name__ == "__main__":
    draw()
