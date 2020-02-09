import pygame as pg
import random
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

size = [800, 480]
width = size[0]
height = size[1]


def run():
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    MOVESPEED = 5
    PLAYERSIZE = 50

    FOODCHECK = 0
    FOODSPAWN = 20
    FOODSIZE = 20

    player = pg.Rect(10, 10, PLAYERSIZE, PLAYERSIZE)

    foods = []
    for i in range(0, FOODSPAWN):
        foods.append(pg.Rect(random.randint(0, width - FOODSIZE),
                             random.randint(0, height - FOODSIZE), FOODSIZE, FOODSIZE))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    moveRight = False
                    moveLeft = True
                if event.key == pg.K_RIGHT:
                    moveRight = True
                    moveLeft = False
                if event.key == pg.K_UP:
                    moveUp = True
                    moveDown = False
                if event.key == pg.K_DOWN:
                    moveUp = False
                    moveDown = True

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    moveLeft = False
                if event.key == pg.K_RIGHT:
                    moveRight = False
                if event.key == pg.K_UP:
                    moveUp = False
                if event.key == pg.K_DOWN:
                    moveDown = False

        FOODCHECK += 1
        if FOODCHECK >= FOODSPAWN:
            FOODCHECK = 0
            foods.append(pg.Rect(random.randint(0, width - FOODSIZE),
                                 random.randint(0, height - FOODSIZE), FOODSIZE, FOODSIZE))

        GAME.fill(BLACK)

        if moveDown and player.bottom < height:
            player.top += MOVESPEED
        elif moveUp and player.top > 0:
            player.top -= MOVESPEED
        elif moveLeft and player.left > 0:
            player.left -= MOVESPEED
        elif moveRight and player.right < width:
            player.left += MOVESPEED

        pg.draw.rect(GAME, WHITE, player)

        for food in foods:
            if player.colliderect(food):
                foods.remove(food)

        for i in range(len(foods)):
            pg.draw.rect(GAME, GREEN, foods[i])

        pg.display.update()
        FPS.tick(60)


if __name__ == "__main__":
    global GAME, FPS

    pg.init()
    GAME = pg.display.set_mode(size)
    pg.display.set_caption('Sample')
    FPS = pg.time.Clock()

    run()
