import pygame


screen_width = 800
screen_height = 600

player_speed = 5

enemy_speed_x = 4
enemy_speed_y = 40
num_enemies = 6

#Images
bullet_image = pygame.image.load('images/bullet.png')
background_image = pygame.image.load('images/background.png')
icon = pygame.image.load('images/ufo.png')
player_image = pygame.image.load('images/player.png')
enemy_image = pygame.image.load('images/enemy.png')
