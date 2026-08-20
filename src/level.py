import pygame

class Level:

    def __init__(self):
        self.platforms = [
            pygame.Rect(0, 500, 800, 100),
            pygame.Rect(900, 450, 300, 50),
            pygame.Rect(1400, 350, 400, 50),
            pygame.Rect(1900, 500, 800, 100),
        ]

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)