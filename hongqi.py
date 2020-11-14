import turtle

turtle.bgcolor("red")
turtle.fillcolor("yellow")
turtle.color('yellow')
turtle.speed(10)
#主星
turtle.begin_fill()
turtle.up()
turtle.goto(-600,220)
turtle.down()
for i in range (5):
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()

#第1颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-400,295)
turtle.setheading(305)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()


#第2颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-350,212)
turtle.setheading(30)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)
turtle.begin_fill()
turtle.up()
turtle.goto(-200,112)
turtle.setheading(30)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()
