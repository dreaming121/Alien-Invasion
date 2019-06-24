import pygame


class Ships(object):

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('D:\Python\image\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #浮点型位置转换
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        #移动标志
        self.up = False
        self.down = False
        self.right = False
        self.left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed
        if self.up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.ship_speed
        if self.down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed
        #更新centerx和bottom
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom