import turtle


def draw_koch_segment(turt, lenght):
    if lenght < 6:
        turt.forward(lenght)
        turt.left(60)
        turt.forward(lenght)
        turt.right(120)
        turt.forward(lenght)
        turt.left(60)
        turt.forward(lenght)
    else:
        new_lenght = lenght // 3
        draw_koch_segment(turt, new_lenght)
        turt.left(60)
        draw_koch_segment(turt, new_lenght)
        turt.right(120)
        draw_koch_segment(turt, new_lenght)
        turt.left(60)
        draw_koch_segment(turt, new_lenght)


natashka = turtle.Turtle()
natashka.speed(100)
natashka.hideturtle()
draw_koch_segment(natashka, 100)
natashka.left(120)
draw_koch_segment(natashka, 100)
natashka.left(120)
draw_koch_segment(natashka, 100)
turtle.done()

