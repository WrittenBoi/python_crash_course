import sys
import pygame
from bullet import Bullet

def fire_event_handle(bullets, ai_settings, screen, ship):
    if(len(bullets) < ai_settings.bullet_max):
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def quit_game():
    print("Quit game, bye!")
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

            elif event.key == pygame.K_SPACE:
                fire_event_handle(bullets, ai_settings, screen, ship)

            elif event.key == pygame.K_q:
                quit_game()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if(bullet.rect.bottom <= 0):
            bullets.remove(bullet)
    #print(len(bullets))

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()
