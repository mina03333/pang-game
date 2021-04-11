import pygame

pygame.init()  # this resets. absolubtely necessary!

# screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title of the screen
pygame.display.set_caption("Nostalgic Arcade Game")

# loop
running = True  # is the game still going?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # checks whether the display should close
            running = False

# if the game ends, pygame ends as well
pygame.quit()
