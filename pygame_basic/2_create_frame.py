import pygame

pygame.init()  # this resets. absolubtely necessary!

# screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title of the screen
pygame.display.set_caption("Nostalgic Arcade Game")

# background image
# background = pygame.image.load("C:/Usersijham/OneDrive/Desktop/PythonWorkspace/pygame_basic/background.png")

# loop
running = True  # is the game still going?
while running:
    for event in pygame.event.get():  # what event happened?
        if event.type == pygame.QUIT:  # checks whether the display should close
            running = False  # game has stopped running

    screen.fill((0, 0, 255))
    # screen.blit(background(0, 0))  # drawing background

    pygame.display.update()  # update game screen


# if the game ends, pygame ends as well
pygame.quit()
