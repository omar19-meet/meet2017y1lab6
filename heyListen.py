import turtle
##turtle.shape('turtle')
####square=turtle.clone
##square.shape('square')

def down():
    global direction
    direction=DOWN
    print("You moved down!")
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x,y-10)
    print(turtle.pos())
    
def left():
    global direction
    direction=LEFT
    print("You moved left!")
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x-10,y)
    print(turtle.pos())

def up():
    global direction
    direction=UP
    print("You moved up!")
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x,y+10)
    print(turtle.pos())

def right():
    global direction
    direction=RIGHT
    print("You moved right!")
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x+10,y)
    print(turtle.pos())
######################################################################

UP_ARROW= "Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"

UP=0
LEFT=1
DOWN=2
RIGHT=3
direction=UP

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(turtle.stamp, SPACEBAR)
turtle.listen()

