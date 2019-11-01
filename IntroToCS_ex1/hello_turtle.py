#############################################################
# FILE : hello_turtle.py
# WRITER : Nadav Weisler , Weisler , 316493758
# EXERCISE : intro2cs ex1 2019
# DESCRIPTION: Draw 3 flowers using "turtle" library
#############################################################


import turtle


def draw_petal():
    """ Draw Petal, diameter - 100 degrees - 90 """
    turtle.circle(100, 90)
    turtle.left(90)
    turtle.circle(100, 90)


def draw_flower():
    """Draw flower, 4 petals"""
    turtle.setheading(0)
    draw_petal()
    turtle.setheading(90)
    draw_petal()
    turtle.setheading(180)
    draw_petal()
    turtle.setheading(270)
    draw_petal()
    turtle.setheading(270)
    turtle.forward(250)


def draw_flower_advance():
    """Draw flower and turning turtle head for draw more flowers"""
    #draw flower
    draw_flower()
    turtle.right(90)
    turtle.up()
    #set turtle position for next flowers
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    """Draw 3 flowers"""
    #set turtle position before drawing 3 flowers
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    #Draw 3 flowers
    for i in range(3):
        draw_flower_advance()


if __name__ == '__main__':
    draw_flower_bed()
    turtle.done()

