import turtle,time
from Game_Elements import Food, Snake, ScoreBoard, Board

# setting up the screen
screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME 🐍🐍')
screen.tracer(0)

# determine the level of game
messages = ['easy','medium','hard']
message = 'choose'
while message not in messages:
    message = screen.textinput('Difficulty level','Easy, Medium or Hard: ').lower()
    if message == messages[0]:
        time_gap = 0.2
    elif message == messages[1]:
        time_gap = 0.1
    elif message == messages[2]:
        time_gap = 0.05

# setting up the snake
snake = Snake()
snake.create_snake()
screen.update()
time.sleep(time_gap)

# setting keys to control snake
screen.listen()
screen.onkey(fun=snake.up,key='Up')
screen.onkey(fun=snake.down,key='Down')
screen.onkey(fun=snake.left,key='Left')
screen.onkey(fun=snake.right,key='Right')

# setting the food, scoreboard and drawing board of game
food = Food()
scoreboard = ScoreBoard()
board = Board()

is_game_on = True
while is_game_on:
    scoreboard.score_update()
    snake.move_snake()
    screen.update()
    time.sleep(time_gap)
    if snake.is_out_of_board() or snake.iscollided():
        is_game_on = False
        scoreboard.gameover()

    if snake.snake_segments[-1].distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        snake.extend()
        screen.update()
screen.exitonclick()
