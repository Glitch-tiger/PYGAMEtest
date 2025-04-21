import pygame
from ability import *

class Character:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)  
        self.speed = 5
#-----------------------------------------------
        self.health = 10  # Начальное здоровье
        self.score = 0  # Начальный счёт
        self.isAlive = True
        self.survival_time = 0
#-----------------------------------------------  
        self.ability = Ability1()  

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def shoot(self):
        color = (0, 255, 0)   
        size = 10             
        self.ability.shoot(self.rect.centerx - size // 2,
                           self.rect.top,
                           color,
                           size)   

    def update_bullets(self):
        self.ability.update_bullets()   
#-----------------------
    def draw(self, surface):
        if self.health >0:
            pygame.draw.rect(surface, (255, 0, 0), self.rect)  
            self.ability.draw(surface)
        else:
            self.isAlive = False   
#-----------------------