import pygame
from src.settings import (PLAYER_SIZE, PLAYER_SPEED, PLAYER_JUMP_VELOCITY, GRAVITY)

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.velocity_x *= 0.8
        if (keys[pygame.K_a] or keys[pygame.K_q] or keys[pygame.K_LEFT]):
            self.velocity_x = -PLAYER_SPEED
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self.velocity_x = PLAYER_SPEED
        if (keys[pygame.K_w] or keys[pygame.K_z] or keys[pygame.K_UP]):
            if self.on_ground:
                self.velocity_y = PLAYER_JUMP_VELOCITY
                self.on_ground = False

    def update(self, platforms):
        self.on_ground = False
        self.velocity_y += GRAVITY
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        for platform in platforms:

            if self.rect.colliderect(platform):
                if self.velocity_y > 0:
                    self.rect.bottom = platform.top
                    self.velocity_y = 0
                    self.on_ground = True
                # IF WE HIT THE BOTTOM OF THE PLATFORM
                elif self.velocity_y < 0:
                    self.rect.top = platform.bottom
                    self.velocity_y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect, border_radius=8)
        eye_x = self.rect.centerx

        if self.velocity_x > 0:
            eye_x += 5
        elif self.velocity_x < 0:
            eye_x -= 5

        eye_center = (eye_x, self.rect.centery)
        pygame.draw.circle(screen, (255, 255, 255), eye_center, 15)
        pygame.draw.circle(screen, (0, 0, 0), eye_center, 7)