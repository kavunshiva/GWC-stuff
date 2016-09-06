"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
import os


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
 



pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700*2
SCREEN_HEIGHT = 500*2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]

# empty list of balls
balls = []

# geschwindigkeitsbegrenzung
speed_limit = [5, 5]


# BOUNCING BALL CLASS CODE  

class BouncingBall(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size
        self.color = possible_ball_colors[random.randint(0, len(possible_ball_colors) - 1)]

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, screen_width, screen_height):

        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, self.color, [self.x_location, self.y_location], self.ball_size)

class BouncingCoder(BouncingBall):

    def __init__(self, x, y, vx, vy, ball_size, picture):
        BouncingBall.__init__(self, x, y, vx, vy, ball_size)
        self.image = pygame.image.load(os.path.join('', picture))

    def move(self, scr, scr_wid, scr_h):
        if self.x_location >= scr_wid - self.ball_size or self.x_location < self.ball_size:
                    self.x_speed = self.x_speed * -1

        if self.y_location >= scr_h - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed

        screen.blit(self.image, (self.x_location, self.y_location))

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            '''
            ball = BouncingBall(pos[0], pos[1], random.randint(-speed_limit[0],speed_limit[0]), \
                                random.randint(-speed_limit[1],speed_limit[1]), random.randint(20,80))
            '''
            ball = BouncingCoder(pos[0], pos[1], random.randint(-speed_limit[0],speed_limit[0]), \
                                random.randint(-speed_limit[1],speed_limit[1]), \
                                random.randint(20,80), 'dms.jpg')
            balls.append(ball)
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here
     
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN) 
    
    # --- Drawing code should go here
    for ball in balls:
        # ball.flashBounce(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        ball.move(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


