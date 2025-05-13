import pygame
from settings import*

def draw_health_and_score(display_surface, player):
    font = pygame.font.Font(None, 36)  # Шрифт
    health_text = font.render(f'Health: {player.health}', True, (0, 0, 0))
    score_text = font.render(f'Score: {player.score}', True, (0, 0, 0))
    timer_text = font.render(f'Timer: {player.survival_time}', True, (0, 0, 0))
    display_surface.blit(health_text, (10, 10))  # Отображение здоровья
    display_surface.blit(score_text, (10, 50))  # Отображение счёта
    display_surface.blit(timer_text, (10, 100))  # Отображение времени

def draw_game_over(display_surface):
    display_surface.fill(WHITE)
    font = pygame.font.Font(None, 74)  # Шрифт для сообщения
    game_over_text = font.render('Ты умер))', True, (255, 0, 0))  # Красный цвет
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Центрируем текст
    display_surface.blit(game_over_text, text_rect)  # Отображаем текст
