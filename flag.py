import turtle

def fillMainSquares(fill_color, x, y):

    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.showturtle()
    turtle.pendown()

    turtle.pencolor(fill_color)
    turtle.color(fill_color)
    turtle.begin_fill()

    turtle.forward(100)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
 
    turtle.end_fill()

def fillSmallSquares(fill_color, x, y):

    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.showturtle()
    turtle.pendown()

    turtle.pencolor(fill_color)
    turtle.color(fill_color)
    turtle.begin_fill()

    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
 
    turtle.end_fill()
   

def dammachakra(x, y):
   
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.showturtle()
    turtle.pendown()

    turtle.speed(3)

    turtle.pensize(2)
    turtle.pencolor('DarkOrange4')

    turtle.color('DarkOrange4', 'DarkOrange3')
    turtle.begin_fill()
    
    # draw the spokes

    heading = 0
    for i in range(8):
        turtle.forward(150)
        turtle.left(25)
        turtle.forward(20)
        turtle.left(135)
        turtle.forward(20)
        turtle.left(25)
        turtle.forward(150)

        heading = heading + 45
        turtle.setheading(heading)

    turtle.end_fill()

    turtle.color('DarkOrange3')
    # raise pen
    turtle.up()

    # head down
    turtle.setheading(270)

    # go forward 20
    turtle.forward(20)

    # reset heading
    turtle.setheading(0)
    
    # pen down
    turtle.down()

    turtle.pensize(5)
    
    # draw the circle
    turtle.circle(20)

    # raise pen
    turtle.up()
    # head down
    turtle.setheading(270)

    # go forward 20
    turtle.forward(100)
    
    # reset heading
    turtle.setheading(0)

    # pen down
    turtle.down()

    turtle.pensize(20)
    # draw the circle
    turtle.circle(120)

    
    
wn = turtle.Screen()
wn.setup(1200, 750) 
wn.title("By Sashin")

turtle.pensize(3)
turtle.speed(4)

fillMainSquares('blue', -500, -150)
fillMainSquares('yellow', -400, -150)
fillMainSquares('red', -300, -150)
fillMainSquares('white', -200, -150)
fillMainSquares('orange', -100, -150)

fillSmallSquares('blue', 0, 170)
fillSmallSquares('yellow', 0, 90)
fillSmallSquares('red', 0, 10)
fillSmallSquares('white', 0, -70)
fillSmallSquares('orange', 0, -150)

dammachakra(-250, 50)






