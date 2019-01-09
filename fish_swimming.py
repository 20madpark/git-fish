import turtle, time, random, math

# screen size parameters
SIZE_X = 900
SIZE_Y = 500
MIN_Y = -200
MAX_Y = 200
MIN_X = -380
MAX_X = 360
WIDTH = 45  # width of the fish graphic
STEP = 5

# initial turtle settings
turtle.hideturtle()
turtle.penup()
turtle.setup(SIZE_X, SIZE_Y)
turtle.goto(0,300)

# pictures for the game
turtle.bgpic("diver3.gif") # background picture
turtle.register_shape("fish.gif") # fish picture
 
# create a piece of food
food = turtle.clone()
food.shape("square") # set the food to be a square shape
food.color("red") # set the food to be red
food.goto(-50,50)
food.showturtle()

# a function which moves a piece of food
# randomly around the screen
def move_food():
	# get the current coordinates
	x_now = food.xcor()
	y_now = food.ycor()
	# make random motion
	x_step = random.randint(-1,1)
	y_step = random.randint(-1,1)
	# set new coordinates
	x_next = x_now + x_step
	y_next = y_now + y_step

	# check to make sure the new x and y values are on the screen
	if x_next > MIN_X and x_next < MAX_X:
		x = x_next
	else:
		x = x_now

	if y_next > MIN_Y and y_next < MAX_Y:
		y = y_next
	else:
		y = y_now
	
	# move the food to the new position	
	food.goto(x,y)

# define the player
player = turtle.clone()
player.goto(50,50)
player.shape("fish.gif") # set the player to be a fish
player.showturtle()

# define the key bindings

def move_right():
	if player.xcor() < MAX_X:
		x,y = player.pos()
		player.goto(x+5,y)

turtle.onkeypress(move_right,"Right")

def move_left():
	if player.xcor() > MIN_X:
		x,y = player.pos()
		player.goto(x-5,y)

turtle.onkeypress(move_left,"Left")

def move_down():
	if player.xcor() > MIN_Y:
		x,y = player.pos()
		player.goto(x,y-5)

turtle.onkeypress(move_down,"Down")

def move_up():
	if player.xcor() < MAX_Y:
		x,y = player.pos()
		player.goto(x,y+5)

turtle.onkeypress(move_up,"Up")


text1=turtle.clone()
text1.penup()
text1.goto(-200,100)
text1.write("Press Space To Start The Game ", font=('Arial', 23, 'normal'))

def check_collision():
	# write your own code here!!!
	# can you figure out how to check whether the player
	# has collided with the food or not?
	# BONUS: how would you keep score?
	pass

# new sprites can be animated by adding function calls inside play_game()
def play_game():
	move_food()
	check_collision()
	turtle.ontimer(play_game,0)

play_game()
turtle.listen()
turtle.mainloop() # function to keep the turtle window open
