import turtle 

turtle.Screen().bgcolor("blue")

sc = turtle.Screen()
sc.setup(400,300)

turtle.title("Welcome to Turtle Windows")

board = turtle.Turtle()

for i in range(12):
    board.forward(100)
    board.left(90)
    i = i+1