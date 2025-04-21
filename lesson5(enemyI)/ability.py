import pygame
import sys
import time

# Класс пули
class Bullet:
    def __init__(self, x, y, color, size, direction):
        self.rect = pygame.Rect(x, y, size, size)  # Прямоугольник для пули
        self.color = color  # Цвет пули
        self.speed = 5  # Скорость пули
        self.direction = direction  # Направление движения (вектор)
        self.creation_time = time.time()  # Время создания пули

    def update(self):
        self.rect.x += self.direction[0] * self.speed  # Двигаем пулю по оси X
        self.rect.y += self.direction[1] * self.speed  # Двигаем пулю по оси Y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)  # Рисуем пулю

    def is_alive(self):
        return (time.time() - self.creation_time) < 3  # Проверяем время жизни пули
    
# Класс способности
class Ability:
    def __init__(self):
        self.bullets = []  # Список для хранения пуль

    def shoot(self, x, y):
        raise NotImplementedError("Метод 'shoot' должен быть реализован в подклассе.")

    def update_bullets(self):
        for bullet in list(self.bullets):  # Используем list() для безопасного удаления элементов из списка во время итерации
            bullet.update()  # Обновляем каждую пулю
            if not bullet.is_alive():  # Удаляем пулю если она вышла за пределы времени жизни
                self.bullets.remove(bullet)

    def draw(self, surface):
        for bullet in self.bullets:
            bullet.draw(surface)  # Рисуем каждую пулю

class Ability1(Ability):
    def shoot(self, x, y, color=(0, 255, 0), size=5):
        directions = [
            (0, -1),   # Вверх
            (0, 1),    # Вниз
            (-1, 0),   # Влево
            (1, 0)     # Вправо
        ]
        
        for direction in directions:
            bullet = Bullet(x, y, color, size, direction)  # Создаём пулю с заданными параметрами
            self.bullets.append(bullet)  # Добавляем пулю в список

class Ability2(Ability):
    def shoot(self, x, y, color=(255, 0, 0), size=10):
        direction = (0, -1)  # Направление вверх
        bullet = Bullet(x, y, color, size, direction)  # Создаём пулю с заданными параметрами
        self.bullets.append(bullet)  # Добавляем пулю в список