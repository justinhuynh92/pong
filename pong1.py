import turtle

# create window
wn = turtle.Screen()
wn.title("Pong by Justin H")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# main game loop
while True:
    # updates the screen every time the loop runs
    wn.update()
