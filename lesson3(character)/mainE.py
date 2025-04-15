import pygame
import sys
from pygame.locals import QUIT
from settings import*
from character import Character

def main():
    pygame.init()
    player = Character(375, 275)

    # Установка размеров окна и создание поверхности для отображения
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Установка заголовка окна
    pygame.display.set_caption('КРУТАЯ ПРОГРАММА')
    clock = pygame.time.Clock()
    
    # Главный игровой цикл
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()  
                sys.exit()
            # Обработка нажатий клавиш
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1     
        player.move(dx, dy)

        # Сюда вставляем код, если хотим отрисовать объект до обновления экрана
        DISPLAYSURF.fill(WHITE) 
        pygame.draw.rect(DISPLAYSURF, (RED), (150, 100, 100, 100))
        player.draw(DISPLAYSURF)
        
        # Обновление экрана с текущими отрисованными объектами
        pygame.display.update()
        clock.tick(FPS)
        # Сюда вставляем код, если хотим отрисовать объект после обновления экрана

if __name__ == "__main__":
    main()
    