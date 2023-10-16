import random

import pygame as pg


class Meteorite(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("./pgt/pj/meteorite.png")
        size = random.randint(70, 150)

        self.image = pg.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.topleft = (800, random.randint(0, 600 - size))

        self.speedx = random.randint(1,5)
        self.speedy = random.randint(-1,1)

    def update(self):
        self.rect.x -= self.speedx
        
        self.rect.y += self.speedy
       


class Mouse_starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("./pgt/pj/enemy.png")
        size = random.randint(70, 150)

        self.image = pg.transform.scale(self.image, (size, size))
        self.image = pg.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midbottom = (random.randint(0, 600 - size), 0)

        self.speedx = random.randint(-1, +1)
        self.speedy = random.randint(1, 2)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Laser(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("./pgt/pj/laser.png")

        self.image = pg.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect(midbottom=pos)

        self.speed = 2

    def update(self):
        self.rect.y -= self.speed


class Starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("./pgt/pj/spaceship rotated.png")
        self.image = pg.transform.scale(self.image, (100, 100))
        self.image = pg.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midleft = (0, 300)

        self.mode = "vertical"
        self.lives = 3

        self.speed = 5

    def update(self):
        keys = pg.key.get_pressed()
        if self.mode == "horizontal":
            if keys[pg.K_a]:
                self.rect.x -= self.speed
            if keys[pg.K_d]:
                self.rect.x += self.speed

        if self.mode == "vertical":
            if keys[pg.K_w]:
                self.rect.y -= self.speed
            if keys[pg.K_s]:
                self.rect.y += self.speed

    def switch_mode(self):
        self.image = pg.image.load("./pgt/pj/spaceship.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (400, 580)

        self.mode = "horizontal"


class Captain(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("./pgt/pj/captain.png")
        self.image = pg.transform.scale(self.image, (400, 400))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30, 600)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = "stay"


class Alien(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("./pgt/pj/alien.png")
        self.image = pg.transform.scale(self.image, (400, 400))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30, 600)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = "stay"
