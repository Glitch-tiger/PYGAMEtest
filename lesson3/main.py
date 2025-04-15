import pygame
import sys
from pygame.locals import QUIT

def main():
    # Инициализация Pygame
    pygame.init()
    
    # Установка размеров окна и создание поверхности для отображения
    DISPLAYSURF = pygame.display.set_mode((400, 300))
    
    # Установка заголовка окна
    pygame.display.set_caption('КРУТАЯ ПРОГРАММА')
    
    # Главный игровой цикл
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == QUIT:  # Проверка на событие выхода
                pygame.quit()  # Завершение Pygame
                sys.exit()     # Выход из программы

        # Сюда вставляем код, если хотим отрисовать объект до обновления экрана
        DISPLAYSURF.fill((255, 255, 255))
        pygame.draw.circle(DISPLAYSURF, (255, 255, 0), (200, 150), 10)
        # Обновление экрана с текущими отрисованными объектами
        pygame.display.update()
        
        # Сюда вставляем код, если хотим отрисовать объект после обновления экрана

# Запуск функции main при выполнении скрипта
if __name__ == "__main__":
    main()
    