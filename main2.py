import pygame
import sys
from pygame.locals import QUIT
#--------------------------------------
from settings import*
#--------------------------------------
def main():
    # Инициализация Pygame
    pygame.init()
    #--------------------------------------
    # Установка размеров окна и создание поверхности для отображения
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #--------------------------------------
    # Установка заголовка окна
    pygame.display.set_caption('КРУТАЯ ПРОГРАММА')
    
    # Главный игровой цикл
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == QUIT:  # Проверка на событие выхода
                pygame.quit()  # Завершение Pygame
                sys.exit()     # Выход из программы

        # Сюда вставляем код для отрисовки объектов до обновления экрана
        #--------------------------------------
        DISPLAYSURF.fill(WHITE)  # Заполнение фона белым цветом
        pygame.draw.rect(DISPLAYSURF, (RED), (150, 100, 100, 100))  # Рисуем зеленый квадрат
        #--------------------------------------
        # Обновление экрана с текущими отрисованными объектами
        pygame.display.update()
        
        # Сюда вставляем код для отрисовки объектов после обновления экрана
       
# Запуск функции main при выполнении скрипта
if __name__ == "__main__":
    main()
