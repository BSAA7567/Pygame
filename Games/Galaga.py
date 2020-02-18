import pygame
import sys
import random
from time import sleep

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

Size = [440, 480]
Width = Size[0]
Height = Size[1]


def writeScore(count):
    font = pygame.font.Font(None, 25)
    text = font.render('Destory enemy: ' + str(count), True, white)
    GAME.blit(text, (10, 0))


def writePassed(count):
    font = pygame.font.Font(None, 25)
    text = font.render('Miss enemy: ' + str(count), True, red)
    GAME.blit(text, (Width - 130, 0))


def writeMessage(text):
    textfront = pygame.font.Font(None, 60)
    textRender = textfront.render(text, True, (255, 0, 0))
    if text == 'Crash!':
        GAME.blit(textRender, (Width//2 - 60, Height//2))
    else:
        GAME.blit(textRender, (Width//2 - 120, Height//2))
    pygame.display.update()
    sleep(2)
    run()


def crash():
    writeMessage('Crash!')


def gameOver():
    writeMessage('Game Over!')


def drawObject(obj, x, y):
    GAME.blit(obj, (x, y))


def run():
    global fighter, missile, explosion, enemy

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x = Width//2
    y = Height - fighterHeight
    fighterX = 0

    missileXY = []

    enemySize = enemy.get_rect().size
    enemyWidth = enemySize[0]
    enemyHeight = enemySize[1]

    enemyX = random.randrange(0, Width - enemyWidth)
    enemyY = 0
    enemySpeed = 3

    isShot = False
    shotCount = 0
    enemyPassed = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    fighterX -= 7

                elif event.key == pygame.K_RIGHT:
                    fighterX += 7

                elif event.key == pygame.K_SPACE:
                    missileX = x + fighterWidth//2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])

            if event.type == pygame.KEYUP:
                  if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        fighterX = 0

        GAME.fill(black)

        x += fighterX
        if x < 0:
            x = 0
        if x > Width - fighterWidth - 10:
            x = Width - fighterWidth - 10

        if y < enemyY + enemyHeight:
            if(enemyX > x and enemyX < x + fighterWidth) or \
                    (enemyX + enemyWidth > x and enemyX + enemyWidth < x + fighterWidth):
                crash()

        drawObject(fighter, x, y)

        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                if bxy[1] < enemyY:
                    if bxy[0] > enemyX and bxy[0] < enemyX + enemyWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        writeScore(shotCount)

        enemyY += enemySpeed

        if enemyY > Height:
            enemySize = enemy.get_rect().size
            enemyWidth = enemySize[0]
            enemyHeight = enemySize[1]
            enemyX = random.randrange(0, Width - enemyWidth)
            enemyY = 0
            enemyPassed += 1

        if enemyPassed == 4:
            gameOver()

        writePassed(enemyPassed)

        if isShot:
            drawObject(explosion, enemyX, enemyY)
            enemySize = enemy.get_rect().size
            enemyWidth = enemySize[0]
            enemyHeight = enemySize[1]
            enemyX = random.randrange(0, Width - enemyWidth)
            enemyY = 0
            isShot = False

            enemySpeed += 0.3
            if enemySpeed >= 10:
                enemySpeed = 10

        drawObject(enemy, enemyX, enemyY)

        pygame.display.update()
        FPS.tick(60)


if __name__ == "__main__":
    global GAME, FPS, fighter, missile, explosion, enemy

    pygame.init()
    GAME = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption('Galaga')
    fighter = pygame.image.load('./imgs/fighter.png')
    missile = pygame.image.load('./imgs/missile.png')
    explosion = pygame.image.load('./imgs/explosion.png')
    enemy = pygame.image.load('./imgs/enemy.png')
    FPS = pygame.time.Clock()

    run()
