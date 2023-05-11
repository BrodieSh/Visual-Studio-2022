
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
WIDTH = 500 #Width of game window 
HEIGHT = 500 #Height of game window 
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

#    _____ _____  _____  _____ _______ ______  _____ 
#   / ____|  __ \|  __ \|_   _|__   __|  ____|/ ____|
#  | (___ | |__) | |__) | | |    | |  | |__  | (___  
#   \___ \|  ___/|  _  /  | |    | |  |  __|  \___ \ 
#   ____) | |    | | \ \ _| |_   | |  | |____ ____) |
#  |_____/|_|    |_|  \_\_____|  |_|  |______|_____/ 
                                                   
                                                   
all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
 
player = Player()
all_sprites.add(player)


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

#   UPDATE
    all_sprites.update()
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()













pygame.quit()
