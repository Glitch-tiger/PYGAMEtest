import pygame
import sys
from pygame.locals import QUIT
from settings import*
from character import Character
#----------------------
import random
from enemy import Mob
#----------------------

def main():
    pygame.init()
    player = Character(175, 250)
#---------------    
    vampires = []  # Список для вампиров
#---------------
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    player.shoot()  
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
#------------------------------        
        # Логика спавна вампиров
        if random.random() < 0.02:  # 2% шанс создания вампира на каждом кадре
            vampires.append(Mob.spawn())
         # Обновление вампиров
        for vampire in vampires[:]:  # Итерируемся по копии списка
            vampire.move(player)      # Движение вампира
            vampire.update(player)  # Обновление состояния вампира
 #           vampire.update_bullets()   # Обновление пуль вампира (если они есть)
            # Удаляем вампира, если он мертв
            if not vampire.alive:
                vampires.remove(vampire)
#------------------------------ 
        # Сюда вставляем код, если хотим отрисовать объект до обновления экрана
        DISPLAYSURF.fill(WHITE) 
        player.update_bullets()   # Обновляем пули
        player.draw(DISPLAYSURF)   # Рисуем персонажа и пули
#------------------------------         
        for vampire in vampires:
            vampire.draw(DISPLAYSURF)
#------------------------------ 
        # Обновление экрана с текущими отрисованными объектами
        pygame.display.update()
        clock.tick(FPS)
        # Сюда вставляем код, если хотим отрисовать объект после обновления экрана

if __name__ == "__main__":
    main()
    