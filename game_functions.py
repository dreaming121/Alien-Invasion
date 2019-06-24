import sys
import pygame
from bullet import Bullet


def check_keydown(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.right = True
    if event.key == pygame.K_LEFT:
        ship.left = True
    if event.key == pygame.K_UP:
        ship.up = True
    if event.key == pygame.K_DOWN:
        ship.down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets = bullets.add(new_bullet)


def check_keyup(event, ship):
    if event.key == pygame.K_UP:
        ship.up = False
    if event.key == pygame.K_DOWN:
        ship.down = False
    if event.key == pygame.K_RIGHT:
        ship.right = False
    if event.key == pygame.K_LEFT:
        ship.left = False


def check_event(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)
    print(len(bullets))