import turtle


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white") # 100
        self.shape("square") # 100
        self.shapesize(5, 1) # 100

    def start(self, horizontal, vertical):
        self.speed("fastest")
        self.penup() # 100
        self.goto(horizontal, vertical) # 100
        self.pendown() # 100

    def up(self):
        #self.setheading()
        if self.ycor()<240:
            self.penup()
            self.sety(self.ycor()+20)
            self.pendown()


    def down(self):
        #self.setheading(270)
        if self.ycor()>-210:
            self.penup()
            self.sety(self.ycor() -20)
            self.pendown()

