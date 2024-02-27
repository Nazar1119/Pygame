import pygame
import random

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((640, 360), flags=pygame.NOFRAME)
pygame.display.set_caption("Can you alive?")
icon = pygame.image.load("images/icon1.png").convert_alpha()

ghost = pygame.image.load("images/ghost.png").convert_alpha()
skull = pygame.image.load("images/bone-2.png").convert_alpha()
super_skull = pygame.image.load("images/skull.png").convert_alpha()
super_skull1 = pygame.transform.flip(super_skull, True, False).convert_alpha()

ghost_list_in_game = []
wolf_list_in_game = []
super_skuls_list_in_game = []
super_skulls_list2 = []
skulls = []

lives_in_game = 0

skulls_left = 1
super_s = 0
killed_items = 0

pygame.display.set_icon(icon)
player_speed = 5
player_x = 130
player_y = 217

gameplay = True

is_jump = False
jump_c = 7

title_font = pygame.font.Font("fonts/font2.ttf", 50)
title = title_font.render("ALIVE SKULL", True, "White")
label = pygame.font.Font("fonts/font2.ttf", 100)
label_restart = pygame.font.Font("fonts/font2.ttf", 55)
lose_label = label.render("YOU LOSE!", False, "Black")
restart = label_restart.render("RESTART GAME", True, "green")
restart_rect = restart.get_rect(topleft=(330, 190))
font = pygame.font.Font("fonts/font2.ttf", 30)

win_font = pygame.font.Font("fonts/font2.ttf", 65)
win_f = win_font.render("Congrats", False, "white")

you_w = pygame.font.Font("fonts/font2.ttf", 65)
you = you_w.render("You win!", False, "white")

again_n = pygame.font.Font("fonts/font2.ttf", 70)
again = again_n.render("Again", False, "green")
again_rect = again.get_rect(topleft=(300, 190))

start_n = pygame.font.Font("fonts/font2.ttf", 110)
start1 = start_n.render("Start", False, (22, 27, 30))
start_rect = start1.get_rect(topleft=(320, 95))

quit_n = pygame.font.Font("fonts/font2.ttf", 70)
quit1 = quit_n.render("Quit", True, "red")
quit_rect = quit1.get_rect(topleft=(380, 200))

quit_n2 = pygame.font.Font("fonts/font2.ttf", 50)
quit2 = quit_n2.render("Quit", True, "red")
quit_rect2 = quit2.get_rect(topleft=(425, 275))



back = pygame.image.load("images/back2.jpeg").convert_alpha()
back1 = pygame.image.load("images/back1.jpeg").convert_alpha()
back2 = pygame.image.load("images/back4.jpeg").convert_alpha()

back_sound = pygame.mixer.Sound("sounds/saund.mp3")
back_sound.play()

numb_w = 27
numb_g = 27
wolf_rand = random.randint(2000, 4000)
ghost_rand = random.randint(6000, 8000)
skull_rand_y = random.randint(170, 265)

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, ghost_rand)

wolf_timer = pygame.USEREVENT + 1
pygame.time.set_timer(wolf_timer, wolf_rand)

bullets_timer = pygame.USEREVENT + 1
pygame.time.set_timer(bullets_timer, 2500)

skull_timer = pygame.USEREVENT + 3
pygame.time.set_timer(skull_timer, 8000)


walking_up = [pygame.image.load("spirit_up/spirit_up1.png").convert_alpha(),
              pygame.image.load("spirit_up/spirit_up2.png").convert_alpha(),
              pygame.image.load("spirit_up/spirit_up3.png").convert_alpha()]

walking_down = [pygame.image.load("Spirit_down/spirit_down1.png").convert_alpha(),
                pygame.image.load("Spirit_down/spirit_down2.png").convert_alpha(),
                pygame.image.load("Spirit_down/spirit_down3.png").convert_alpha()]

walk_right = [
        pygame.image.load("spirite_right/walk1.png").convert_alpha(),
        pygame.image.load("spirite_right/walk2.png").convert_alpha(),
        pygame.image.load("spirite_right/walk3.png").convert_alpha(),
        pygame.image.load("spirite_right/walk4.png").convert_alpha(),
        pygame.image.load("spirite_right/walk5.png").convert_alpha(),
        pygame.image.load("spirite_right/walk6.png").convert_alpha(),
        pygame.image.load("spirite_right/walk7.png").convert_alpha(),
        pygame.image.load("spirite_right/walk8.png").convert_alpha(),
        pygame.image.load("spirite_right/walk9.png").convert_alpha(),
]

walk_left = [
        pygame.image.load("spirite_left/walk1.png").convert_alpha(),
        pygame.image.load("spirite_left/walk2.png").convert_alpha(),
        pygame.image.load("spirite_left/walk3.png").convert_alpha(),
        pygame.image.load("spirite_left/walk4.png").convert_alpha(),
        pygame.image.load("spirite_left/walk5.png").convert_alpha(),
        pygame.image.load("spirite_left/walk6.png").convert_alpha(),
        pygame.image.load("spirite_left/walk7.png").convert_alpha(),
        pygame.image.load("spirite_left/walk8.png").convert_alpha(),
        pygame.image.load("spirite_left/walk9.png").convert_alpha(),
]

wolf = [
        pygame.image.load("wolf/wolf1.png").convert_alpha(),
        pygame.image.load("wolf/wolf2.png").convert_alpha(),
        pygame.image.load("wolf/wolf3.png").convert_alpha(),
        pygame.image.load("wolf/wolf4.png").convert_alpha(),
        pygame.image.load("wolf/wolf5.png").convert_alpha(),
]
wolf_count = 0

player_count = 0
player_count_down = 0
bg_x = 0


run = True
win = False
start = False


while run:
    screen.blit(back, (bg_x, 0))
    screen.blit(back, (bg_x + 640, 0))
    screen.blit(title, (15, 20))
    text = font.render("Score: " + str(killed_items), True, "black")
    text1 = font.render("Monsters in : " + str(lives_in_game), True, "black")
    screen.blit(text, (15, 80))
    screen.blit(text1, (15, 110))


    if gameplay and lives_in_game < 4 and not win and (numb_w > 0 and numb_g > 0) and start:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        if ghost_list_in_game:
            for (i, elem) in enumerate(ghost_list_in_game):
                screen.blit(ghost, elem)
                elem.x -= 7
                if elem.x < -20:
                    ghost_list_in_game.pop(i)
                    lives_in_game += 1
                if player_rect.colliderect(elem):
                    gameplay = False


        if wolf_list_in_game:
            for (i, elem) in enumerate(wolf_list_in_game):
                screen.blit(wolf[wolf_count], elem)
                elem.x -= 4.5
                if elem.x < -20:
                    wolf_list_in_game.pop(i)
                    lives_in_game += 1
                if player_rect.colliderect(elem):
                    gameplay = False

        if super_skuls_list_in_game:
            for(i, elem) in enumerate(super_skuls_list_in_game):
                screen.blit(super_skull1, elem)
                elem.x -= 3
                if elem.x < -20:
                    super_skuls_list_in_game.pop(i)
                if player_rect.colliderect(elem):
                    super_s += 1
                    super_skuls_list_in_game.pop(i)


        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            screen.blit(walk_right[player_count], (player_x, player_y))
        elif keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_count], (player_x, player_y))
        elif keys[pygame.K_UP]:
            screen.blit(walking_up[player_count_down], (player_x, player_y))
        elif keys[pygame.K_DOWN]:
            screen.blit(walking_down[player_count_down], (player_x, player_y))
        else:
            screen.blit(walk_right[player_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 600:
            player_x += player_speed
        elif keys[pygame.K_UP] and player_y > 205:
            player_y -= 3
        elif keys[pygame.K_DOWN] and player_y < 240:
            player_y += 3# ruh

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_c >= -7:
                if jump_c > 0:
                    player_y -= (jump_c ** 2) / 2
                else:
                    player_y += (jump_c ** 2) / 2
                jump_c -= 1
            else:
                is_jump = False
                jump_c = 7#jump


        if player_count_down == 2:
            player_count_down = 0
        else:
            player_count_down += 1

        if player_count == 8:
            player_count = 0
        else:
            player_count += 1

        if wolf_count == 4:
            wolf_count = 0
        else:
            wolf_count += 1

        bg_x -= 2
        if bg_x == -640:
            bg_x = 0#kadru

        if skulls:
            for (i, elem) in enumerate(skulls):
                screen.blit(skull, (elem.x, elem.y))
                elem.x += 7
                if elem.x > 660:
                    skulls.pop(i)
                if ghost_list_in_game:
                    for (index, ghost1) in enumerate(ghost_list_in_game):
                        if elem.colliderect(ghost1):
                            killed_items += 1
                            ghost_list_in_game.pop(index)
                            skulls.pop(i)
                            # if killed_items >= 2:
                            #     gameplay = False
                            #     win = True
                if wolf_list_in_game:
                    for(index_w, wolf1) in enumerate(wolf_list_in_game):
                        if elem.colliderect(wolf1):
                            killed_items += 1
                            wolf_list_in_game.pop(index_w)
                            skulls.pop(i)
                            # if killed_items >= 2:
                            #     gameplay = False
                            #     win = True
            if killed_items >= 30:
                gameplay = False
                win = True

        if super_skulls_list2:
            for(i, elem) in enumerate(super_skulls_list2):
                screen.blit(super_skull, (elem.x, elem.y))
                elem.x += 7
                if elem.x > 660:
                    super_skulls_list2.pop(i)
                if ghost_list_in_game:
                    for (index, ghost2) in enumerate(ghost_list_in_game):
                        if elem.colliderect(ghost2):
                            ghost_list_in_game.pop(index)
                            killed_items += 1

                if wolf_list_in_game:
                    for (index, wolf1) in enumerate(wolf_list_in_game):
                        if elem.colliderect(wolf1):
                            wolf_list_in_game.pop(index)
                            killed_items += 1

            if killed_items >= 30:
                gameplay = False
                win = True

    elif win:
        screen.fill((255, 148, 0))
        screen.blit(back1, (0, 0))
        screen.blit(win_f, (295, 50))
        screen.blit(you, (410, 110))
        screen.blit(again, again_rect)
        screen.blit(quit2, quit_rect2)
        back_sound.stop()

        mouse1 = pygame.mouse.get_pos()
        if again_rect.collidepoint(mouse1) and pygame.mouse.get_pressed()[0]:
            player_x = 110
            ghost_list_in_game.clear()
            wolf_list_in_game.clear()
            skulls.clear()
            super_skuls_list_in_game.clear()
            super_skulls_list2.clear()
            skulls_left = 1
            super_s = 0
            lives_in_game = 0
            killed_items = 0
            numb_g = 27
            numb_w = 27
            back_sound.play()
            skull_rand_y = random.randint(175, 265)
            gameplay = True
            win = False
        if quit_rect2.collidepoint(mouse1) and pygame.mouse.get_pressed()[0]:
            run = False

    elif not start:
        screen.blit(back2, (0, 0))
        screen.blit(start1, start_rect)
        screen.blit(quit1, quit_rect)
        back_sound.stop()

        mouse1 = pygame.mouse.get_pos()
        if start_rect.collidepoint(mouse1) and pygame.mouse.get_pressed()[0]:
            player_x = 110
            ghost_list_in_game.clear()
            wolf_list_in_game.clear()
            skulls.clear()
            super_skuls_list_in_game.clear()
            super_skulls_list2.clear()
            skulls_left = 1
            super_s = 0
            lives_in_game = 0
            killed_items = 0
            numb_g = 27
            numb_w = 27
            back_sound.play()
            skull_rand_y = random.randint(175, 265)
            gameplay = True
            win = False
            start = True
        if quit_rect.collidepoint(mouse1) and pygame.mouse.get_pressed()[0]:
            run = False

    else:
        screen.fill((255, 148, 0))
        screen.blit(back1, (0, 0))
        screen.blit(lose_label, (283, 60))
        screen.blit(restart, restart_rect)
        screen.blit(quit2, quit_rect2)
        back_sound.stop()


        mouse = pygame.mouse.get_pos()
        if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 110
            ghost_list_in_game.clear()
            wolf_list_in_game.clear()
            skulls.clear()
            super_skuls_list_in_game.clear()
            super_skulls_list2.clear()
            skulls_left = 1
            super_s = 0
            numb_g = 27
            numb_w = 27
            lives_in_game = 0
            killed_items = 0
            back_sound.play()
            skull_rand_y = random.randint(175, 265)
            gameplay = True
        if quit_rect2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == ghost_timer and numb_g > 0:
            ghost_list_in_game.append(ghost.get_rect(topleft=(660, 195)))
            numb_g -= 1
        if event.type == wolf_timer and numb_w > 0:
            wolf_list_in_game.append(wolf[wolf_count].get_rect(topleft=(660, 255)))
            numb_w -= 1
        if event.type == bullets_timer:
            skulls_left += 1
        if event.type == skull_timer:
            super_skuls_list_in_game.append(super_skull1.get_rect(topleft=(660, skull_rand_y)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_a and skulls_left > 0:
            skulls.append(skull.get_rect(topleft=(player_x + 20, player_y + 10)))
            skulls_left -= 1
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_d and super_s > 0:
            super_skulls_list2.append(super_skull.get_rect(topleft=(player_x + 20, player_y + 10)))
            super_s -= 1
    pygame.display.update()
    clock.tick(30)
pygame.quit()