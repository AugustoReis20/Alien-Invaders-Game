import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

#screen size value variable
x = 1280
y = 720

#variable screen size and game name
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Alien Invaders")

#background variable 
bg = pygame.image.load("./images/background.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

#alien variable
alien = pygame.image.load("./images/alien.png").convert_alpha()
alien = pygame.transform.scale(alien, (120, 120))

#player variable(or spaceship)
playerImg = pygame.image.load("./images/spaceship.png").convert_alpha()
playerImg = pygame.transform.scale(playerImg, (90, 90))
playerImg = pygame.transform.rotate(playerImg, 360)

#missil variable
missil = pygame.image.load("./images/missile.png").convert_alpha()
missil = pygame.transform.scale(missil, (50, 50))
missil = pygame.transform.rotate(missil, 135)

#background music variable
backgroundmusic = pygame.mixer.music.load("./audio/Amadeus Mozart - K 626 Confutatis [Requiem] [8 bits].mp3")
pygame.mixer.music.play(-1)

#alien position value variable
pos_alien_x = 465
pos_alien_y = 65

#player position(or spaceship) value variable
pos_player_x = 600
pos_player_y = 625

#position value variable with missile speed
vel_x_missil = 0
pos_x_missil = 598
pos_y_missil = 625

#score variable
points = 4

#non-automatic trigger variable
triggered = False

#screen loop variable
run = True

#font variable
font = pygame.font.SysFont("./fonts/VerminVibes1989Regular.ttf", 50)

#variable of rectangular guides of collision markings
player_rect = playerImg.get_rect()
alien_rect = alien.get_rect()
missil_rect = missil.get_rect()

#respawn and collision functions
def respawn():
    x = 1
    y = random.randint(1, 1200)
    return [x, y]


def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_x_missil = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_x_missil]


def collisons():
    global points
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        points -= 1
        return True
    elif missil_rect.colliderect(alien_rect):
        points += 1
        return True
    else:
        return False

#loop while and conditional (screen, track time, spaceship(player) and missile keys, respawns, collisions,... score.)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #function to make background appear
    screen.blit(bg, (0, 0))
    
    #frames per second variable
    clock = pygame.time.Clock()
    FPS = 300

    #vertical screen movement disabled
    #rel_x = x % bg.get_rect().height
    #screen.blit(bg, (0, rel_x - bg.get_rect().height))
    #if rel_x < 1280:
        #screen.blit(bg, (0, rel_x))

    #key conditionals
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_LEFT] and pos_player_x > 1:
        pos_player_x -= 15
        if not triggered:
            pos_x_missil -= 15

    if tecla[pygame.K_RIGHT] and pos_player_x < 1230:
        pos_player_x += 15
        if not triggered:
            pos_x_missil += 15

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_missil = 10

    #score conditional less than zero
    if points == 0:
        run = False

    #respawns conditional
    if pos_alien_y > 720:
        random_y = random.randint(1, 1)
        random_x = random.randint(1, 1260)
        pos_alien_y = random_y
        pos_alien_x = random_x

    if pos_y_missil < 1:
        pos_x_missil, pos_y_missil, triggered, vel_x_missil = respawn_missil()

    if pos_alien_y == 50 or collisons():
        pos_alien_x = respawn()[1]
        pos_alien_y = respawn()[0]

    #loop of the movements of objects
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.x = pos_x_missil
    missil_rect.y = pos_y_missil

    alien_rect.x = pos_alien_x
    alien_rect.y = pos_alien_y

    #screen movement speed disabled
    #x += 1
    #alien and missile speed
    pos_alien_y += 10
    pos_y_missil -= vel_x_missil

    #marking guides for collisions disabled
    #pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)
    #pygame.draw.rect(screen, (255, 0, 0), missil_rect, 4)
    #pygame.draw.rect(screen, (255, 0, 0), alien_rect, 4)

    #score creation variable
    score = font.render(f" Points: {int(points)} ", True, (255, 255, 255))
    screen.blit(score, (50, 50))

    #static method of the clock
    clock.tick(FPS)

    #function to make objects appear
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_x_missil, pos_y_missil))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    #appearance of the score on the screen
    print(points)

    #update screen
    pygame.display.update()
