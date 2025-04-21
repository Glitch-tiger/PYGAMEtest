import pygame
import random
from settings import*
from ability import*

class Mob:
    def __init__(self, x, y):
        self.rect = pygame.Rect(
            random.choice([-50, SCREEN_WIDTH + 50]),  # Спавн за пределами экрана
            random.randint(0, SCREEN_HEIGHT),  # Спавн по вертикали в пределах экрана
            50, 50  # Размер вампира
        )
        self.speed = 2  # Скорость вампира
        self.alive = True  # Состояние вампира (жив/мертв)
        self.ability = Ability2

    def move(self, target):
        if self.alive:
            if target.rect.centerx < self.rect.centerx:
                self.rect.x -= self.speed
            elif target.rect.centerx > self.rect.centerx:
                self.rect.x += self.speed

            if target.rect.centery < self.rect.centery:
                self.rect.y -= self.speed
            elif target.rect.centery > self.rect.centery:
                self.rect.y += self.speed

    def shoot(self):
        color = (0, 255, 0)   
        size = 2             
        self.ability.shoot(self.rect.centerx - size // 2,
                           self.rect.top,
                           color,
                           size)   

#    def update_bullets(self):
#        """Обновление пуль вампира."""
#        self.ability.update_bullets()   

    def update(self, character):
        """Обновление состояния вампира."""
        if not self.alive:
            return
        
        if self.rect.colliderect(character.rect):  # Столкновение с персонажем
            #character.alive = False  # Персонаж умирает
            self.alive = False  # Вампир тоже умирает
        
        for bullet in character.ability.bullets:  # Итерируемся по пулям способности персонажа
            if self.rect.colliderect(bullet.rect):  # Проверка на столкновение с пулей
                self.alive = False  # Вампир умирает от пули
                break

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, (255, 0, 0), self.rect)  

    @classmethod
    def spawn(cls):
        return cls(random.choice([-50, SCREEN_WIDTH + 50]), random.randint(0, SCREEN_HEIGHT))