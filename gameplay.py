def move_forward():
    print("Moving forward...")


def move_backward():
    print("Moving backward...")


def turn_left():
    print("Turning left...")


def turn_right():
    print("Turning right...")


def stop():
    print("Stopping...")


def light():
    print("Opening light...")


def gameplay_function(action):
    if action == "forward":
        move_forward()
    elif action == "backward":
        move_backward()
    elif action == "left":
        turn_left()
    elif action == "right":
        turn_right()
    elif action == "stop":
        stop()
    elif action == "light":
        light()    