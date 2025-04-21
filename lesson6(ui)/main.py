import pygame
import random
import sys
from pygame.locals import QUIT
from settings import*
from character import Character
from enemy import Mob
#-----------------------------------------------
from ui import*
#----------------------------------------------


def main():
    pygame.init()
    player = Character(175, 250)  
    vampires = []
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('КРУТАЯ ПРОГРАММА')
    clock = pygame.time.Clock()
    
    # Главный игровой цикл
    while True:
        start_ticks = 0
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
        player.survival_time = (pygame.time.get_ticks() - start_ticks) / 1000  # Время в секундах
        # Логика спавна вампиров
        if random.random() < 0.02:
            vampires.append(Mob.spawn())
        for vampire in vampires[:]:
            vampire.move(player) 
            vampire.update(player) 
 #           vampire.update_bullets()   # Обновление пуль вампира (если они есть)
 
            if not vampire.alive:
                vampires.remove(vampire)

        # Сюда вставляем код, если хотим отрисовать объект до обновления экрана
        DISPLAYSURF.fill(WHITE) 
        player.update_bullets()   # Обновляем пули
        player.draw(DISPLAYSURF)   # Рисуем персонажа и пули
        for vampire in vampires:
            vampire.draw(DISPLAYSURF)
#-----------------------------------------------
        # Отображение здоровья и счёта
        draw_health_and_score(DISPLAYSURF, player)
        if not player.isAlive:
            draw_game_over(DISPLAYSURF)    
#-----------------------------------------------
        # Обновление экрана с текущими отрисованными объектами
        pygame.display.update()
        clock.tick(FPS)
        # Сюда вставляем код, если хотим отрисовать объект после обновления экрана

if __name__ == "__main__":
    main()
    