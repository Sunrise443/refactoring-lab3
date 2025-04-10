import random
import pygame
from pygame import mixer

from game_objects import Player, Enemy, Bullet
from util import show_score, game_over_text, is_collision
import resources

def main():
    pygame.init()

    screen = pygame.display.set_mode((resources.screen_width, resources.screen_height))
    pygame.display.set_caption("Space Invader")
    pygame.display.set_icon(resources.icon)
    mixer.music.load("music/background.wav")
    mixer.music.play(-1)

    player = Player()
    bullet = Bullet()
    enemies = [Enemy() for _ in range(resources.num_enemies)]

    score = 0

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(resources.background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x_change = -player.speed
                if event.key == pygame.K_RIGHT:
                    player.x_change = resources.player_speed
                if event.key == pygame.K_SPACE:
                    if bullet.state == "ready":
                        bullet_sound = mixer.Sound("music/laser.wav")
                        bullet_sound.play()
                        bullet.fire(player.x)
            
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player.x_change = 0

        player.update()
        bullet.update()

        game_over = False
        for enemy in enemies:
            enemy.update()

            if is_collision(enemy, bullet):
                explosion_sound = mixer.Sound("music/explosion.wav")
                explosion_sound.play()
                bullet.state = "ready"
                score += 1
                enemy.x = random.randint(0, resources.screen_width-64)
                enemy.y = random.randint(50, 150)

            if enemy.y > 440:
                game_over = True

        if game_over:
            game_over_text(screen)
            for enemy in enemies:
                enemy.y = 2000

        player.draw(screen)
        bullet.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        show_score(screen, score)

        pygame.display.update()

if __name__ == "__main__":
    main()
