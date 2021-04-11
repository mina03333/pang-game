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

# character moving direction
character_to_x = 0

# character moving speed
character_speed = 5

# create weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# can shoot multiple times
weapons = []

# weapon moving speed
weapon_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2. event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # character to the left
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # character to the right
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:  # weapon shooting
                weapon_x_pos = character_x_pos + \
                    (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. character location
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # weapon location
    # 100, 200 -> 180, 160, 140, ...
    # 500, 200 -> 180, 160, 140, ...
    weapons = [[w[0], w[1] - weapon_speed]
               for w in weapons]  # weapon to the top

    # weapon reaching to the top -> disappear
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 4. bump

    # 5. screen drawing
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
