import random

import resources

class Player:
    def __init__(self):
        self.img = resources.player_image
        self.x = 370
        self.y = 480
        self.speed = resources.player_speed
        self.x_change = 0

    def update(self):
        self.x += self.x_change
        if self.x <= 0:
            self.x = 0
        elif self.x >= resources.screen_width - 64:
            self.x = resources.screen_width - 64

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

class Enemy:
    def __init__(self):
        self.img = resources.enemy_image
        self.x = random.randint(0, resources.screen_width - 64)
        self.y = random.randint(50, 150)
        self.speed_x = resources.enemy_speed_x
        self.speed_y = resources.enemy_speed_y

    def update(self):
        self.x += self.speed_x
        if self.x <= 0 or self.x >= resources.screen_width - 64:
            self.speed_x *= -1
            self.y += self.speed_y

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

class Bullet:
    def __init__(self):
        self.img = resources.bullet_image
        self.x = 0
        self.y = 480
        self.speed = 10
        self.state = "ready"
    
    def fire(self, player_x):
        if self.state == "ready":
            self.x = player_x
            self.state = "fire"
    
    def update(self):
        if self.state == "fire":
            self.y -= self.speed
            if self.y <= 0:
                self.state = "ready"
                self.y = 480
                
    def draw(self, screen):
        if self.state =="fire":
            screen.blit(self.img, (self.x+16, self.y+10))
