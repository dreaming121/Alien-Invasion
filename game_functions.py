import sys
import pygame


def check_keydown(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.right = True
    if event.key == pygame.K_LEFT:
        ship.left = True
    if event.key == pygame.K_UP:
        ship.up = True
    if event.key == pygame.K_DOWN:
        ship.down = True


def check_keyup(ship, event):
    if event.key == pygame.K_UP:
        ship.up = False
    if event.key == pygame.K_DOWN:
        ship.down = False
    if event.key == pygame.K_RIGHT:
        ship.right = False
    if event.key == pygame.K_LEFT:
        ship.left = False


def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(ship, event)
        elif event.type == pygame.KEYUP:
            check_keyup(ship, event)


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
