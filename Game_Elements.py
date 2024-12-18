from turtle import Turtle
import random

class Snake:
    def __init__(self):
        self.snake_segments = []

    def create_snake(self):
        step = 0
        for i in range(4):
            square = Turtle('square')
            square.up()
            square.setposition(step,0)
            square.color('white')
            self.snake_segments.append(square)
            step += 20 # each square 20 units apart to constitute a snake

    def move_snake(self):
        for segment_num in range(len(self.snake_segments)-1):
            self.snake_segments[segment_num].goto(self.snake_segments[segment_num+1].pos())
        self.snake_segments[-1].forward(20)
    
    def hide(self):
        for snake_segment in self.snake_segments:
            snake_segment.hideturtle()

    def up(self):
        if self.snake_segments[-1].heading() != 270:
            self.snake_segments[-1].setheading(90)
    
    def down(self):
        if self.snake_segments[-1].heading() != 90:
            self.snake_segments[-1].setheading(270)

    def right(self):
        if self.snake_segments[-1].heading() != 180:
            self.snake_segments[-1].setheading(0)
    
    def left(self):
        if self.snake_segments[-1].heading() != 0:
            self.snake_segments[-1].setheading(180)

    def is_out_of_board(self):
        if self.snake_segments[-1].pos()[0] > 290 or self.snake_segments[-1].pos()[1] > 290 or self.snake_segments[-1].pos()[0] < -290 or self.snake_segments[-1].pos()[1] < -290:
            return True
        return False

    def extend(self):
        square = Turtle('square')
        square.up()
        
        if self.snake_segments[0].heading() in (0,180):
            square.setposition(self.snake_segments[0].xcor()-20,self.snake_segments[0].ycor())
        else:
            square.setposition(self.snake_segments[0].xcor(),self.snake_segments[0].ycor()-20)
        square.setheading(self.snake_segments[0].heading())
        square.color('white')
        self.snake_segments.insert(0,square)

    def iscollided(self):
        for segment_num in range(len(self.snake_segments)-1):
            if self.snake_segments[-1].distance(self.snake_segments[segment_num]) < 10:
                return True
        return False

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.6,stretch_wid=0.6)
        self.color('blue')
        self.speed('fastest')
        self.goto(random.randint(-250,250),random.randint(-250,250))
    
    def refresh(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))

from turtle import Turtle
class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.up()
        with open('snake.txt') as file:
            highscore = file.read()
        self.highscore = int(highscore)
        self.hideturtle()
        self.goto(0,290)
        self.color('white')

    def score_update(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}',align='center',font=('Arial',20,'normal'))

    def gameover(self):
        
        if self.score >= self.highscore:
            self.highscore = self.score
            with open('snake.txt','w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.score_update()

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.up()
        self.goto(-290,-290)
        self.down()
        self.pensize(5)
        for i in range(4):
            self.forward(580)
            self.left(90)