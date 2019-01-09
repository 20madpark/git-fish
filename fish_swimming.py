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
        x_step = random.randint(-10,10)
        y_step = random.randint(-10,10)
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

xpos = 50
ypos = 50
xvel = 0
yvel = 0

# define the player
player = turtle.clone()
player.goto(xpos,ypos)
player.shape("fish.gif") # set the player to be a fish
player.showturtle()

# define the key bindings

def update_values():
        global xpos
        global ypos
        global xvel
        global yvel
        x,y = player.position()
        if(x + xvel >= MAX_X):
                x = MAX_X
        elif(x + xvel <= MIN_X):
                x = MIN_X
        else:
                x += xvel
        if(y + yvel >= MAX_Y):
                y = MAX_Y
        elif(y + yvel <= MIN_Y):
                y = MIN_Y
        else:
                y += yvel
        if(xvel > 0):
                xvel -= 0.2
        elif(xvel < 0):
                xvel += 0.2
        if(yvel > 0):
                yvel -= 0.2
        elif(yvel < 0):
                yvel += 0.2
        player.goto(x,y)

def move_right():
        global xvel
        xvel = 5

turtle.onkeypress(move_right,"Right")

def move_left():
        global xvel
        xvel = -5

turtle.onkeypress(move_left,"Left")

def move_down():
        global yvel
        yvel = -5

turtle.onkeypress(move_down,"Down")

def move_up():
        global yvel
        yvel = 5

turtle.onkeypress(move_up,"Up")


text1=turtle.clone()
text1.penup()
text1.goto(-200,100)
text1.write("Press Space To Start The Game ", font=('Arial', 23, 'normal'))

def check_collision():
        playerpos = player.position()
        playerx = playerpos[0]
        playery = playerpos[1]
        playerx1 = playerx - 25
        playerx2 = playerx + 25
        playery1 = playery + 25
        playery2 = playery - 25
        fishpos = food.position()
        fishx = fishpos[0]
        fishy = fishpos[1]
        fishx1 = fishx - 10
        fishx2 = fishx + 10
        fishy1 = fishy + 10
        fishy2 = fishy - 10
        if(playerx2 > fishx1 and playerx1 < fishx2 and playery2 < fishy1 and playery1 > fishy2):
                return True
        else:
                return False
        # write your own code here!!!
        # can you figure out how to check whether the player
        # has collided with the food or not?
        # BONUS: how would you keep score?

# new sprites can be animated by adding function calls inside play_game()
def play_game():
        update_values()
        move_food()
        if(check_collision() == True):
                food.hideturtle()
        turtle.ontimer(play_game,0)

play_game()
turtle.listen()
turtle.mainloop() # function to keep the turtle window open
