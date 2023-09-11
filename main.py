import pygame
import pencil
pygame.init()
screen_height = 1280
screen_width = 720
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Paint tool")
draw_on = False
last_pos = (0, 0)
#Radius of the brush
radius = 8


clock = pygame.time.Clock()
running = True
screen.fill("green")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Selecting random color code
            color = (0, 0, 0)
            pygame.draw.circle(screen, color, event.pos, radius)
            draw_on = True
            #When mouse button is released it will stop drawing
        if event.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        if event.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(screen, color, event.pos, radius)
                pencil.roundline(screen, color, event.pos, last_pos, radius)
            last_pos = event.pos
    

#Render YOUR GAME HERE
#flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(80) 
pygame.quit()

