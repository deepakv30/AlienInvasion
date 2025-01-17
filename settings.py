class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game settings"""
        # Screen Settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        #Ship Settings
        # self.ship_speed = 1.5
        # self.bg_color = (0, 0, 255)
        #Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        #Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50
        
        
