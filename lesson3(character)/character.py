import pygame
class Character:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)  # Прямоугольник для персонажа
        self.speed = 5  # Скорость движения

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0) , self.rect)  # Рисуем персонажа