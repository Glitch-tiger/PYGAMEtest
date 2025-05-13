import pygame
import random
import sys
import os
from pygame.locals import QUIT
from settings import*
from character import Character
from enemy import Mob
from ui import*



def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('КРУТАЯ ПРОГРАММА')
    clock = pygame.time.Clock()
    
    #Загрузка файлов
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bg_path = os.path.join(script_dir, 'asset', 'bg.png')
    v_path = os.path.join(script_dir, 'asset', 'v.png')
    p_path = os.path.join(script_dir, 'asset', 'm.png')
    background_image = pygame.image.load(bg_path).convert()
    enemy_image = pygame.image.load(v_path).convert_alpha()
    player_image = pygame.image.load(p_path).convert_alpha()

    player = Character(175, 250,player_image)  
    vampires = []

    
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
            vampires.append(Mob.spawn(enemy_image))
        for vampire in vampires[:]:
            vampire.move(player) 
            vampire.update(player) 
 #           vampire.update_bullets()   # Обновление пуль вампира (если они есть)
 
            if not vampire.alive:
                vampires.remove(vampire)

        # Сюда вставляем код, если хотим отрисовать объект до обновления экрана
        DISPLAYSURF.blit(background_image, (0, 0)) 
        player.update_bullets()   # Обновляем пули
        player.draw(DISPLAYSURF)   # Рисуем персонажа и пули
        for vampire in vampires:
            vampire.draw(DISPLAYSURF)
        # Отображение здоровья и счёта
        draw_health_and_score(DISPLAYSURF, player)
        if not player.isAlive:
            draw_game_over(DISPLAYSURF)    
        # Обновление экрана с текущими отрисованными объектами
        pygame.display.update()
        clock.tick(FPS)
        # Сюда вставляем код, если хотим отрисовать объект после обновления экрана

if __name__ == "__main__":
    main()
    