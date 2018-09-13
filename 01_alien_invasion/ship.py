import os
import pygame

class Ship():
    """ Class of ship """

    def __init__(self, screen, ai_settings):
        """ init ship obj. """

        # save screen
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image
        self.image = pygame.image.load(
            os.path.join("images", "ship.bmp"))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set init position of ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # float center of ship
        self.center = float(self.rect.centerx)

        # ship move flag
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if(self.moving_left and
                self.rect.left > 0):
            self.center -= self.ai_settings.ship_speed_factor

        elif(self.moving_right and
                self.rect.right < self.screen_rect.right):
            self.center += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """ Refresh ship """
        self.screen.blit(self.image, self.rect)

