import pygame
import random
from cscroll import Scroller

# setup pygame
pygame.init()

# set screen width and height
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# make the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# make the runner!
class RunnerSprite(pygame.sprite.Sprite):

    def __init__(self, color, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def moveYourself(self, pos):    
        self.rect.center = pos

    def update(self):
        self.rect.x -= 3
        if (self.rect.x < 0):
            self.rect.y = random.randint(0, SCREEN_HEIGHT)


# ------------- copied from busy world of mr. anderson --------------

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

# make a clock
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

# set cityscape fore-, mid-, and background colors
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3, screen, SCREEN_WIDTH)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2, screen, SCREEN_WIDTH)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1, screen, SCREEN_WIDTH)

front_scroller.add_buildings()
middle_scroller.add_buildings()
back_scroller.add_buildings()

# add a player
player = RunnerSprite(GREEN,(30, 30))


# make a list of players
all_sprites_list = pygame.sprite.Group()

# add player to player list
all_sprites_list.add(player)

# make list of good sprites
good_sprites = pygame.sprite.Group()

for i in range(10):
    good_sprites.add(RunnerSprite(WHITE, (SCREEN_WIDTH + 100, random.randint(0, SCREEN_HEIGHT))))

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    

    # --- Game logic should go here
    mos_pos = pygame.mouse.get_pos()
    player.moveYourself(mos_pos)
    for sprite in good_sprites:
        sprite.update()

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here

    # draw scrollers    
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()

    # draw sprites
    all_sprites_list.draw(screen)
    good_sprites.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE



