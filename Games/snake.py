import pygame as pg
import sys
import random

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 204, 0)

Size = [400, 350]
width = Size[0]
height = Size[1]

def gameOver():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()            
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    run()

        GAME.fill(black)
        endFont = pg.font.SysFont('times new roman', 60)
        endSurf = endFont.render("Game Over", True, red)
        GAME.blit(endSurf, ((width // 2)-130, (height // 2)-50))

        reFont = pg.font.SysFont('monaco', 40)
        reSurf = reFont.render("Press R restart",True, white)
        GAME.blit(reSurf, ((width // 2) - 100, (height // 2) + 50))

        pg.display.update()

def showScore():
    SFont = pg.font.SysFont('monaco', 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, black)
    GAME.blit(Ssurf, (5,0))

def run():
    global score,speed,level_up

    objSize = 13

    score = 0
    speed = 5
    level_up = 5

    state = ''
    change = ''

    snakeHead = [random.randint(0, width - objSize), random.randint(0, height - objSize)]
    snakeBody = [snakeHead]

    food = [random.randint(0, width - objSize), random.randint(0, height - objSize)]
    foodSpawn = True

    while True:
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

        if score == level_up:
            print('Level up!')
            level_up += 5
            speed += 1

        if foodSpawn == False:
            food = [random.randint(0, width - objSize), random.randint(0, height - objSize)]
            foodSpawn = True

        GAME.fill(white)

        for pos in snakeBody:
            pg.draw.rect(GAME, green, pg.Rect(pos[0], pos[1], objSize, objSize))

        pg.draw.rect(GAME, red, pg.Rect(snakeHead[0], snakeHead[1], objSize, objSize))
        pg.draw.circle(GAME, yellow, (food[0], food[1]),objSize-5)

        if drawHead.bottom > height:
            gameOver()
        elif drawHead.top < 0:
            gameOver()
        elif drawHead.left < 0:
            gameOver()
        elif drawHead.right > width:
            gameOver()

        for tail in snakeBody[1:]:
            if snakeHead == tail:
                gameOver()
        showScore()
        pg.display.update()
        FPS.tick(30)

def main():
    global GAME,FPS

    pg.init()
    GAME = pg.display.set_mode(Size)
    pg.display.set_caption("Snake Game")
    FPS = pg.time.Clock()

    run()

if __name__ == "__main__":
    main()