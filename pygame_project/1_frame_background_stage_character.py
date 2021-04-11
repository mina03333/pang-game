import os
import pygame
##############################################################
# reset
pygame.init()

# background image size set
screen_width = 640  # horizontal
screen_height = 480  # vertical
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("Mina Pang")

# FPS
clock = pygame.time.Clock()
##############################################################

# 1. game reset(background, game images, location, speed, font, etc)
current_path = os.path.dirname(__file__)  # current file location path change
# images folder location chanage
image_path = os.path.join(current_path, "images")

# background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# stage set
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # character placed on the same level as the stage

# create character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

running = True
while running:
    dt = clock.tick(30)

    # 2. event handling (keyboard, mouse, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. character location

    # 4. bump

    # 5. screen drawing
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
