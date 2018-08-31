import pygame
import time
import random

pygame.init()

# In order to use sound for crash funtionality
crash_sound = pygame.mixer.Sound("crash.wav")

# For car game play we use car.wav sound while playing
pygame.mixer.music.load("car.wav")

# For Screen Display width and height of the screen used to display the game
display_width = 800
display_height = 600

# Different color coding used in the program.
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

block_color = (53, 115, 255)

# This variable car_width = 73 is used in the rest of the program to know where both edges of the car are.
# The car's location really just means the location of the top left pixel of the car.
# Because of this, it is helpful to also know where the right side is.

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Car Game')
clock = pygame.time.Clock()

carImage = pygame.image.load('racecar.png')

# Declared paused variable globally
pause = False


def things_dodged(count):
    """
    It is used to increament the counter called Score to run
    and for display we use blit.
    :param count:
    """
    font = pygame.font.SysFont(None, 25)
    text = font.render('Score: ' + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    """
    This function takes x, y starting points, width and height variables
    and finally a color.
    we use pygame.draw.rect() to draw the polygon to our specifications.
    The parameters to this function are : where, what color and
    then the x,y location followed by the width and the height.
    :param thingx:
    :param thingy:
    :param thingw:
    :param thingh:
    :param color:
    """
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImage, (x, y))  # "Blit" basically just draws the image to the screen


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# def message_display(text):
#     largeText = pygame.font.Font('freesansbold.ttf', 80)
#     TextSurf, TextRect = text_objects(text, largeText)
#     TextRect.center = ((display_width/2),(display_height/2))
#     gameDisplay.blit(TextSurf, TextRect)
#
#     pygame.display.update()
#
#     time.sleep(2)
#
#     gameLoop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()

        gameDisplay.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects("You Crashed", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play Again", 150, 400, 100, 50, green, bright_green, gameLoop)
        button("QUIT", 550, 400, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    """

    :param msg: What do you want the button to say on it
    :param x: The x location of the top left coordinate of the button box.
    :param y: The y location of the top left coordinate of the button box.
    :param w: Button width.
    :param h: Button height.
    :param ic: Inactive color (when a mouse is not hovering).
    :param ac: Active color (when a mouse is hovering)
    :param action:
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 18)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():  # Quit Button functionality
    pygame.quit()
    quit()


def unpause():
    pygame.mixer.music.unpause()
    global pause
    pause = False


def paused():
    """
    Sometimes, a player needs to pause for various reasons.
    One method is to freeze the frame and write Pause over
    it with some instructions on how to play again. Another is to have the window cleared and have the Pause and instructions on that. If you think your players might be inclined to cheat by pausing to slow things down, then you might want to clear the screen.
    """

    pygame.mixer.music.pause()      # Pause the already playing music.

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()

        gameDisplay.fill(white)

        # Created for displaying on the screen "Paused"
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        # Button size and dimensions followed by Resume text on button and Quit on the other one.
        button("RESUME", 150, 400, 100, 50, green, bright_green, unpause)
        button("QUIT", 550, 400, 100, 50, red, bright_red, quitgame)
        # Gonna update the display everytime any function is called for specific events.
        pygame.display.update()
        clock.tick(15)


def game_intro():  # Gonna run one time
    """
    here, we're just defining a variable of "intro" as True, and calling a while loop to run until the variable is no longer true.

    Within that loop, we have created a mini-pygame instance, which is currently just displaying a title at 15 frames per second.
    From here, we can, and will, add some actual functional buttons for the player to use and click to play or quit.
    """
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects("Let's Race Over", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("START", 150, 400, 100, 50, green, bright_green, gameLoop)
        button("QUIT", 550, 400, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def gameLoop():
    global pause
    pygame.mixer.music.play(-1)  # -1 for infinity loop for music

    x = (display_width * 0.45)
    y = (display_height * 0.80)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5  # Move 5 times left of current pos
                if event.key == pygame.K_RIGHT:
                    x_change = 5  # Move 5 times right of current pos
                if event.key == pygame.K_p: # add a check if the P key is pressed in the KEYDOWN event if-statement:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0  # No change in position

        x += x_change   # "x" is used to position our car image in the car function.

        gameDisplay.fill(white)  # Paint the window white along with the car.

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x, y)

        things_dodged(dodged)

        if x > display_width - car_width or x < 0:  # Also include car width in order to check it really crashed at edges
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height  # Blocks to show up at once
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1  # Increase Speed of blocks
            thing_width += (dodged * 1.2)  # Increase size of the blocks

        # if y < thing_starty + thing_height: we're asking if y, the car's top left, has crossed the object's y + height, meaning the bottom left.
        # If it has, then, for logic sake, we print that y crossover has occurred.
        # Now, this doesn't mean there's necessarily overlap, maybe the x coordinates are vastly different and
        # we're on opposite sides. So, then we need to ask if the objects are anywhere within each other's boundaries.

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
gameLoop()
pygame.quit()
quit()
