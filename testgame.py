import pygame
import time

pygame.init()

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 320

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect(0,0,32,32)
for i in range(10):
    pygame.draw.line(screen, (0,255,0), (i*32,0), (i*32,320))
    
pygame.key.set_repeat(50)

running = True
while running:
    screen.fill((0,0,0))
    for i in range(10):
        pygame.draw.line(screen, (0,255,0), (i*32,0), (i*32,320))
        pygame.draw.line(screen, (0,255,0), (0,i*32), (320,i*32))

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    
##    if key[pygame.K_UP] and player.y >= 32:
##        player.move_ip(0, -32)
##    elif key[pygame.K_DOWN] and player.y <= 32*8:
##        player.move_ip(0, 32)
##    elif key[pygame.K_LEFT] and player.x >= 32:
##        player.move_ip(-32, 0)
##    elif key[pygame.K_RIGHT] and player.x <= 32*8:
##        player.move_ip(32, 0)

    pressedKeys = pygame.key.get_pressed()
    
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if key[pygame.K_UP] and player.y >= 32:
                player.move_ip(0, -32)
            elif key[pygame.K_DOWN] and player.y <= 32*8:
                player.move_ip(0, 32)
            elif key[pygame.K_LEFT] and player.x >= 32:
                player.move_ip(-32, 0)
            elif key[pygame.K_RIGHT] and player.x <= 32*8:
                player.move_ip(32, 0)

        if event.type == pygame.QUIT:
            running = False
        elif(pressedKeys[pygame.K_q]):
            running = False


    pygame.display.update()
    time.sleep(.01)

pygame.quit()
