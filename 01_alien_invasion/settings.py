class Settings():
    """ Save all settings """

    def __init__(self):
        """ init all settings """
        # Screen settings
        self.screen_width = 600
        self.screen_height = 480
        self.bg_color = (230, 230, 230)
        self.game_title = "Alien Invasion"

        # Ship settings
        self.ship_speed_factor = 3

        # Bullet settings
        self.bullet_max = 5
        self.bullet_speed_factor = 1
        self.bullet_color = (60, 60, 60)
        self.bullet_width = 3
        self.bullet_height = 15
