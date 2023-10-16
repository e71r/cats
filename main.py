import time
from sprite import *


def dialogue_mode(sprite, text):
    sprite.update()
    screen.blit(space, (0,0))
    screen.blit(sprite.image, sprite.rect)


    text1 = fnt.render(text[text_number], True, (255,255,255))

    screen.blit(text1, (280,450))

    if text_number < len(text) - 1:
        text2 = fnt.render(text[text_number+1], True, (255,255,255))

        screen.blit(text2, (280,470))


pg.init()
pg.mixer.init()

size = (800, 600)
screen = pg.display.set_mode(size)
pg.display.set_caption("Космические коты")

FPS = 120
clock = pg.time.Clock()

is_running = True
mode = "start_scene"

space = pg.image.load("./pgt/pj/bg.png")
space = pg.transform.scale(space, (size[0], size[1]))

meteorites = pg.sprite.Group()
mice = pg.sprite.Group()
lasers = pg.sprite.Group()

heart = pg.image.load("./pgt/pj/heart.png").convert_alpha()
heart = pg.transform.scale(heart, (30,30))\

pg.mixer.music.load("./pgt/pj/music.wav")
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play()

laser_sound = pg.mixer.Sound("./pgt/pj/laser.wav")
victory_sound = pg.mixer.Sound("./pgt/pj/victory.wav")

captain = Captain()
alien = Alien()
starship = Starship()

start_text = ["Мы засекли сигнал с планеты Мур.",
              "",
              "Наши друзья, инопланетные коты,",
              "нуждаются в помощи.",
              "Космические мыши хотят съесть их луну,",
              "потому что она похожа на сыр.",
              "Как долго наш народ страдал от них, ",
              "теперь и муряне в беде...",
              "Мы должны помочь им.",
              "Вылетаем прямо сейчас.",
              "Спасибо, что починил звездолёт, штурман. ",
              "Наконец-то функция автопилота работает.",
              "Поехали!"]

alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
              "",
              "Мыши уже начали грызть луну...",
              "Скоро куски луны будут падать на нас.",
              "Спасите муриан!", ]

final_text = ["Огромное вам спасибо,",
              "друзья с планеты Мяу!",
              "Как вас называть? Мяуанцы? Мяуриане?",
              "В любом случае, ",
              "теперь наша планета спасена!",
              "Мы хотим отблагодарить вас.",
              "Капитан Василий и его штурман получают",
              "орден SKYSMART.",
              "А также несколько бутылок нашей",
              "лучшей валерьянки.",
              "",
              ""]

text_number = 0

fnt = pg.font.Font("./pgt/pj/font.otf", 25)


while is_running:

    # СОБЫТИЯ
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.KEYDOWN:
            if mode == "start_scene":
                text_number += 2
                if text_number > len(start_text):
                    text_number = 0
                    mode = "meteorites"
                    start_time = time.time()
            
            if mode == "alien_scene":
                text_number += 2
                if text_number > len(alien_text):
                    text_number = 0
                    mode = "moon"

                    alien.rect.topleft = (-30, 600)

                    alien.mode = "up"
                    starship.switch_mode()

                    start_time = time.time()

            if mode == "final_scene":
                text_number += 2
                if text_number >= len(final_text):
                    text_number = 0
                    quit()
                    

            if mode == "moon":
                if event.key == pg.K_SPACE:
                    lasers.add(Laser(starship.rect.midtop))
                    laser_sound.play()


    # ОБНОВЛЕНИЯ
    if mode == "start_scene":
        dialogue_mode(captain, start_text)

    if mode == "meteorites":

        if time.time() - start_time > 5.0:
            mode = "alien_scene"
            text_number = 0
            starship.lives = 3
            

        if random.randint(1,100) == 1:
            meteorites.add(Meteorite())

        

        hits = pg.sprite.spritecollide(starship, meteorites, True)

        if starship.lives < 1:
            is_running = False

        for hit in hits:
            if hit != None:
                starship.lives -= 1

       

        screen.blit(space, (0,0))

        screen.blit(starship.image, starship.rect)
        meteorites.update()
        meteorites.draw(screen)
        starship.update()

        for i in range(starship.lives):
            screen.blit(heart, (i*30, 0))


    if mode == "alien_scene":
        dialogue_mode(alien, start_text)


    if mode == "moon":
    
        if time.time() - start_time > 5.0:
            mode = "final_scene"
            text_number = 0
            victory_sound.play()

        if random.randint(1,100) == 1:
            mice.add(Mouse_starship())

        lasers.update()


        hits = pg.sprite.spritecollide(starship, mice, True)

        if starship.lives < 1:
            is_running = False

        for hit in hits:
            if hit != None:
                starship.lives -= 1

        hits = pg.sprite.groupcollide(lasers, mice, True, True)

        screen.blit(space, (0,0))

        screen.blit(starship.image, starship.rect)
        lasers.draw(screen)
        mice.update()
        mice.draw(screen)
        starship.update()
       


        for i in range(starship.lives):
            screen.blit(heart, (i*30, 0))

    if mode == "final_scene":
        dialogue_mode(alien, final_text)

    pg.display.flip()
    clock.tick(FPS)
