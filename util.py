import math
import pygame


def show_score(screen, score, x=10, y=10):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(text, (x, y))

def game_over_text(screen, x=200, y=250):
    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render(("GAME OVER", True, (255, 255, 255)))
    screen.blit(text, (x, y))

def is_collision(enemy, bullet):
    distance = math.sqrt(math.pow(enemy.x - bullet.x, 2) + (math.pow(enemy.y - bullet.y, 2)))
    return distance < 27
