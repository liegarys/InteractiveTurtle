import turtle

IsMoveForward = False
penMode = 0



def Forward():
    if IsMoveForward :
        turtle_Ins.forward(10)



def Down():
    turtle_Ins.left(180)


def Right():
    turtle_Ins.right(15)

def Left():
    turtle_Ins.left(15)


def StartMoveForward():
    global  IsMoveForward
    IsMoveForward = True
    Forward()

def StopMoveForward():
    global  IsMoveForward
    IsMoveForward = False


def ClearScreen():
    turtle_Ins.clear()


def PenMode():
    global  penMode
    penMode += 1

    if penMode % 2 == 0 :
        turtle_Ins.pendown()

    else:
        turtle_Ins.penup()



screen = turtle.Screen()
screen.bgcolor("light green")
screen.title("Interactive")

turtle_Ins = turtle.Turtle()

screen.listen()

screen.onkeypress(fun = StartMoveForward, key= "Up")
screen.onkeyrelease(fun= StopMoveForward, key= "Up")

screen.onkeypress(fun = Down, key= "Down")
screen.onkeyrelease(fun= Down, key= "Down")

screen.onkeypress(fun = Left, key= "Left")
screen.onkeyrelease(fun= Left, key= "Left")

screen.onkeypress(fun = Right, key= "Right")
screen.onkeyrelease(fun= Right, key= "Right")


screen.onkey(fun= ClearScreen, key = "c")

screen.onkey(fun = PenMode, key= "p")


screen.mainloop()