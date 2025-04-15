import pygame
import sys
from pygame.locals import QUIT
from settings import*

def main():
    pygame.init()
    
    # Установка размеров окна и создание поверхности для отображения
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Установка заголовка окна
    pygame.display.set_caption('КРУТАЯ ПРОГРАММА')
    
    # Главный игровой цикл
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()  
                sys.exit()     

        # Сюда вставляем код, если хотим отрисовать объект до обновления экрана
        DISPLAYSURF.fill(WHITE) 
        pygame.draw.rect(DISPLAYSURF, (RED), (150, 100, 100, 100))

        # Обновление экрана с текущими отрисованными объектами
        pygame.display.update()
        
        # Сюда вставляем код, если хотим отрисовать объект после обновления экрана

if __name__ == "__main__":
    main()
    