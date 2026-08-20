import pygame
from src.settings import WIDTH, HEIGHT, FPS, SKY
from src.player import Player
from src.level import Level
from src.camera import Camera

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Jump")

        self.clock = pygame.time.Clock()
        self.player = Player(100, 400)
        self.level = Level()
        self.camera = Camera()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.handle_input()
        self.player.update(self.level.platforms)
        self.camera.update(self.player)

    def draw(self):
        self.screen.fill(SKY)
        self.level.draw(self.screen)
        self.player.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()