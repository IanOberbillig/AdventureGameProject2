##import pygame
##import time
##
##pygame.init()
##
##SCREEN_WIDTH = 800
##SCREEN_HEIGHT = 600
##
##screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
##
##running = True
##while running:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##    pressedKeys = pygame.key.get_pressed()
##    if(pressedKeys[pygame.K_a]):
##        print("a is being pressed")
##    else:
##        print("a is not being pressed")
##    pressedButtons = pygame.mouse.get_pressed()
##    if(pressedButtons[0]):
##        print("The left button is being pressed at", pygame.mouse.get_pos())
##    time.sleep(.4)
##
##pygame.quit()
import pygame
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
text_font = pygame.font.SysFont("Arial", 30)

def draw_text(screen, text, font, color, x_position, y_position):
    text_image = text_font.render(text, True, color)
    screen.blit(text_image, (x_position, y_position))
current_text = ""

running = True
while running:
    screen.fill((0,0,0))    # fill the screen with black
    draw_text(screen, current_text, text_font, (0, 255, 0), 100, 100)
    
    #handle key press events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # if the key is in the a-z, add it to the text
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                current_text += event.unicode
        elif event.type == pygame.KEYUP:
            # if the key is in the a-z, remove it from the text (by replacing it with an empty string)
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                current_text = current_text.replace(event.unicode, "")
                
    time.sleep(.01)
    pygame.display.flip()

pygame.quit()

