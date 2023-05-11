
#  ____  ____  ____  ___  ____    ____  _  _  ___    __    __  __  ____ 
# ( ___)(_  _)(  _ \/ __)(_  _)  (  _ \( \/ )/ __)  /__\  (  \/  )( ___)
#  )__)  _)(_  )   /\__ \  )(     )___/ \  /( (_-. /(__)\  )    (  )__) 
# (__)  (____)(_)\_)(___/ (__)   (__)   (__) \___/(__)(__)(_/\/\_)(____)


#PyGame template - skeleton for a new pygame
import pygame
import random 

#  ___  _____  _  _  ____  ____  ___           
# / __)(  _  )( \( )( ___)(_  _)/ __)
#( (__  )(_)(  )  (  )__)  _)(_( (_-.
# \___)(_____)(_)\_)(__)  (____)\___/
WIDTH = 360 #Width of game window 
HEIGHT = 480 #Height of game window 
FPS = 60 #frames per second 

# ____  _  _  ____  ____  ____    __    __    ____  ____  ____ 
#(_  _)( \( )(_  _)(_  _)(_  _)  /__\  (  )  (_  _)(_   )( ___)
# _)(_  )  (  _)(_   )(   _)(_  /(__)\  )(__  _)(_  / /_  )__) 
#(____)(_)\_)(____) (__) (____)(__)(__)(____)(____)(____)(____)
#Initialise pyGame and create window
pygame.init()
pygame.mixer.init() #Sound
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('wasted') #game name
clock = pygame.time.Clock() #setting the clock

#   ___  _____  __    _____  __  __  ____  ___ 
#  / __)(  _  )(  )  (  _  )(  )(  )(  _ \/ __)
# ( (__  )(_)(  )(__  )(_)(  )(__)(  )   /\__ \
#  \___)(_____)(____)(_____)(______)(_)\_)(___/

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)



#   ___    __    __  __  ____    __    _____  _____  ____ 
#  / __)  /__\  (  \/  )( ___)  (  )  (  _  )(  _  )(  _ \
# ( (_-. /(__)\  )    (  )__)    )(__  )(_)(  )(_)(  )___/
#  \___/(__)(__)(_/\/\_)(____)  (____)(_____)(_____)(__)  

running = True
while running:
   # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw / render
    screen.fill(BLACK)
    # *after* drawing everything, flip the display
    pygame.display.flip()
    pygame.display.toggle_fullscreen()

pygame.quit()