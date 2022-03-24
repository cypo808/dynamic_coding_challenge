import pygame, sys, random

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60
W, H = 900, 600
SCREEN = pygame.display.set_mode((W, H)) # make pygame window
TITLE = pygame.display.set_caption("Hangman")
#ICON = pygame.image.load("assets\images\icon.png")
#pygame.display.set_icon(ICON)

colors = {
    "white" : (255, 255, 255),
    "gray" : (20, 20, 20),
    "black" : (0, 0, 0)}

words = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'pink', 'white', 'gray', 'black']







def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        
        CLOCK.tick(FPS)
        pygame.display.update()

main()