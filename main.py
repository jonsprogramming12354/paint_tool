import pygame
pygame.init()
screen_height = 1280
screen_width = 720
screen = pygame.display.set_mode((screen_height, screen_width))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
    screen.fill("green")

#Render YOUR GAME HERE
#flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(80) 
pygame.quit()
def main():
    print("paint tool")
main()
