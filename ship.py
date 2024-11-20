import pygame

class Ship:
    """A class to manage ship"""
    
    def __init__(self, ai_game):
        """Initilize the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # self.ship_speed = ai_game.settings.ship_speed

        """Load the ship image and get it's rect"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        """Start new ship at bottom center of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for ship's horzontal position
        self.x = float(self.rect.x)

        #Movement flgs
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Update the ship's position based on the movement flag"""
        #Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1.5
        if self.moving_left and self.rect.left > 0:
            self.x -= 1.5
        
        #Update rect object from self.x
        self.rect.x = self.x