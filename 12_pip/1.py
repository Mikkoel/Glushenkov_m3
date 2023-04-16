import turtle


class LSystem:
    axiom: str
    state: str
    width: int
    length: int
    angle: int
    turtle: turtle.Turtle
    rules: dict


    def __init__(self, axiom: str,
                 width: int,
                 lenght: int,
                 angle: int,
                 start_position: tuple,
                 start_angle: int):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        turtle.tracer(0, 0)
        self.turtle.penup()
        self.turtle.setposition(start_position)
        self.turtle.setheading(start_angle)
        self.turtle.pendown()
        self.turtle.pensize(width)

        self.axiom = axiom
        self.state = axiom
        self.length = lenght
        self.angle = angle

        self.rules = dict()

    def add_rules(self, *rules: turtle):
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, iteration):
        for _ in range(iteration):
            for key, velue in self.rules.items():
                self.state = self.state.replace(key, velue.lower())
            self.state = self.state.upper()

    def draw(self):
        stack =[]
        for move in self.state:
            if move == "F":
                self.turtle.forward(self.length)
            elif move == "+":
                self.turtle.left(self.angle)
            elif move == "-":
                self.turtle.right(self.angle)
            elif move == "[":
                stack.append((self.turtle.xcor(),
                             self.turtle.ycor(),
                             self.turtle.heading(),
                             self.turtle.pensize()))
            elif move == "]":
                x, y, angle, width = stack.pop()
                self.turtle.penup()
                self.turtle.sety(x)
                self.turtle.sety(y)
                self.turtle.setheading(angle)
                self.turtle.pensize(width)
                self.turtle.pendown()
                self.width = width

        turtle.done()

    @staticmethod
    def prepear(width: int, height: int):
        screen = turtle.Screen()
        screen.setup(width, height)


if __name__ == "__main__":
    LSystem.prepear(1500, 900)

    l_sys = LSystem(axiom='F', width=2,
                    lenght=5, angle=25,
                    start_position=(0, 0),
                    start_angle=90)

    l_sys.add_rules(('F', 'F[+F]F[-F]F'))
    l_sys.generate_path(4)
    l_sys.draw()