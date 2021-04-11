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

# create balls
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# speed
ball_speed_y = [-18, -15, -12, -9]  # index 0, 1, 2, 3 에 해당하는 값

# balls
balls = []

# big ball
balls.append({
    "pos_x": 50,  # x of ball
    "pos_y": 50,  # y of ball
    "img_idx": 0,  # image index of ball
    "to_x": 3,  # if -3, move to the left, if 3, move to the right
    "to_y": -6,  # y movement
    "init_spd_y": ball_speed_y[0]})  # y inital speed

# weapon removed, ball saved
weapon_to_remove = -1
ball_to_remove = -1

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

    # ball location
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # toched the wall -> bounce back
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # vertical
        # stage bounce back
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:  # speed increase
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. bump

    # character rect info update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # ball rect info update
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # ball and character bump check
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # balls and weapons bump check
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # weapon rect info update
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # bump check
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx  # weapon remove
                ball_to_remove = ball_idx  # ball remove
                break

    # bumped weapon or ball removed
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 5. screen drawing
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
