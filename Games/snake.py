import pygame as pg
import sys
import random

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)

Size = [600, 450]
width=Size[0]
height=Size[1]

def showScore():
    SFont = pg.font.SysFont('monaco', 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, black)
    GAME.blit(Ssurf, (5,0))

def run():
    check = True
    global score,speed,level
    objSize = 10
    score = 0
    speed = 5
    level = 5
    state = ''
    change = ''

    snakeHead = [random.randrange(0, width - objSize), random.randrange(0, height - objSize)]
    snakeBody = [snakeHead]

    food = [random.randrange(0, width - objSize), random.randrange(0, height - objSize)]
    foodSpawn = True

    while check:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                check = False
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    change = 'RIGHT'
                if event.key == pg.K_LEFT:
                    change = 'LEFT'
                if event.key == pg.K_UP:
                    change = 'UP'
                if event.key == pg.K_DOWN:
                    change = 'DOWN'

        if change == 'RIGHT' and state != 'LEFT':
            state = 'RIGHT'
        elif change == 'LEFT' and state != 'RIGHT':
            state = 'LEFT'
        elif change == 'UP' and state != 'DOWN':
            state = 'UP'
        elif change == 'DOWN' and state != 'UP':
            state = 'DOWN'

        if state == 'RIGHT':
            snakeHead[0] += speed
        elif state == 'LEFT':
            snakeHead[0] -= speed
        elif state == 'DOWN':
            snakeHead[1] += speed
        elif state == 'UP':
            snakeHead[1] -= speed

        drawHead = pg.Rect(snakeHead[0], snakeHead[1], objSize, objSize)
        drawFood = pg.Rect(food[0], food[1], objSize, objSize)

        snakeBody.insert(0, list(snakeHead))

        if drawHead.colliderect(drawFood):
            foodSpawn = False
            score += 1
        else:
            snakeBody.pop()

        if score == level:
            level += 10
            speed += 1

        if foodSpawn == False:
            food = [random.randrange(1, width - objSize), random.randrange(1, height - objSize)]
            foodSpawn = True

        GAME.fill(white)

        for pos in snakeBody:
            pg.draw.rect(GAME, green, pg.Rect(pos[0], pos[1], objSize, objSize))

        pg.draw.rect(GAME, red, pg.Rect(snakeHead[0], snakeHead[1], objSize, objSize))
        pg.draw.rect(GAME, brown, pg.Rect(food[0], food[1], objSize, objSize))

        if drawHead.bottom > height:
            gameOver()
            check=False
        elif drawHead.top < 0:
            gameOver()
            check=False
        elif drawHead.left < 0:
            gameOver()
            check=False
        elif drawHead.right > width:
            gameOver()
            check=False

        for tail in snakeBody[1:]:
            if snakeHead == tail:
                gameOver()
                check = False
        showScore()
        pg.display.flip()
        FPS.tick(30)

def main():
    global GAME,FPS
    pg.init()

    GAME = pg.display.set_mode(Size)
    pg.display.set_caption("Snake Game")
    FPS = pg.time.Clock()

    check = True
    while check:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                check = False
                sys.exit()

        GAME.fill(black)

        endFont = pg.font.SysFont('Stencil', 85)
        reFont = pg.font.SysFont('monaco', 50)

        GOsurf = endFont.render("SNAKE GAME", True, green)
        GAME.blit(GOsurf, ((width / 2) - 250, (height / 2) - 50))

        pg.draw.rect(GAME, white, pg.Rect((width / 2) - 60, (height / 2) + 90, 120, 50))
        text = reFont.render("START", True, black)
        GAME.blit(text, ((width / 2) - 55, (height / 2) + 100))

        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if ((width / 2) - 60) + 120 > cur[0] > (width / 2) - 60 and ((height / 2) + 90) + 50 > cur[1] > (height / 2) + 90:
            if (click[0] == 1):
                run()
                check=False

        pg.display.flip()

def gameOver():
    check =True
    while check:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                check = False
                sys.exit()

        GAME.fill(black)
        endFont = pg.font.SysFont('times new roman', 72)
        reFont = pg.font.SysFont('monaco', 70)

        GOsurf = endFont.render("Game Over", True, red)
        GAME.blit(GOsurf, ((width / 2) - 150, (height / 2) - 50))

        Ssurf = endFont.render("Score  :  {0}".format(score), True, red)
        GAME.blit(Ssurf, ((width / 2) - 130, (height / 2) + 50))

        pg.draw.rect(GAME, white, pg.Rect((width / 2) - 60, (height / 2) + 150, 120, 50))
        text=reFont.render("RE?",True,black)
        GAME.blit(text, ((width / 2) - 45, (height / 2) + 155))

        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if ((width / 2) - 60)+120>cur[0]>(width / 2)-60 and ((height / 2) + 150)+50>cur[1]>(height / 2)+150:
            if(click[0]==1):
                run()
        pg.display.flip()

main()