import pygame as pg
import sys
import random

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


size=[960,679]
width = size[0]
height = size[1]

pl_x = 130
pl_y = 70

en_x = 150
en_y = 90

def drawsc():
    SFont = pg.font.SysFont('monaco', 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, white)

    game.blit(Ssurf,(0,0))

def crash():
    check = True
    while check:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                check = False
                sys.exit()

        game.fill(black)
        endFont = pg.font.SysFont('times new roman', 72)
        reFont = pg.font.SysFont('monaco', 70)

        GOsurf = endFont.render("Game Over", True, red)
        game.blit(GOsurf, ((width / 2) - 150 , (height / 2) - 50))

        Ssurf = endFont.render("Score  :  {0}".format(score), True, red)
        game.blit(Ssurf, ((width / 2) - 130 , (height / 2) + 50))

        pg.draw.rect(game, white, pg.Rect((width / 2) - 60, (height / 2) + 150, 120, 50))
        text = reFont.render("RE?", True, black)
        game.blit(text, ((width / 2)-45 , (height / 2)+155 ))

        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if ((width / 2) - 60) + 120 > cur[0] > (width / 2) - 60 and ((height / 2) + 150) + 50 > cur[1] > (height / 2) + 150:
            if (click[0] == 1):
                main()
        pg.display.flip()

def drawobj(obj,x,y):
    game.blit(obj,(x,y))

def run():
    global score
    score=0

    isShot = False
    isCon = 0

    x=0
    y=0
    y_ch = 0

    bullet_xy=[]

    back_x=0
    back_x2=width

    enemy_x=width
    enemy_y=random.randrange(0,height-en_y)

    check = True
    while check:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                check = False
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    y_ch = -15
                elif event.key == pg.K_DOWN:
                    y_ch = 15
                elif event.key == pg.K_s:
                    bullet_x = x+pl_x
                    bullet_y = y+pl_y/2
                    bullet_xy.append([bullet_x, bullet_y])

            if event.type == pg.KEYUP:
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    y_ch = 0
        y+=y_ch
        if y<0:
            y=0
        elif y>height-pl_y:
            y=height-pl_y

        back_x-=8
        back_x2-=8
        if back_x == -width:
            back_x=width
        if back_x2 == -width:
            back_x2=width

        enemy_x-=20
        if enemy_x<=0:
            enemy_x = width
            enemy_y = random.randrange(0, height-en_y)

        if len(bullet_xy)!=0:
            for i,bxy in enumerate(bullet_xy):
                bxy[0]+=15
                bullet_xy[i][0]=bxy[0]
                if bxy[0] > enemy_x:
                    if bxy[1] > enemy_y and bxy[1]<enemy_y+en_y:
                        score+=1
                        bullet_xy.remove(bxy)
                        isShot = True
                if bxy[0]>=width:
                    bullet_xy.remove(bxy)

        drawobj(backgr,back_x,0)
        drawobj(backgr2, back_x2, 0)
        drawsc()
        drawobj(player, x, y)

        if x+pl_x > enemy_x:
            if(y > enemy_y and y < enemy_y+en_y) or (y+pl_y > enemy_y and y+pl_y < enemy_y+en_y):
                crash()
                check = False

        if not isShot:
            drawobj(enemy,enemy_x,enemy_y)
        else:
            drawobj(boom,enemy_x,enemy_y)
            isCon+=1
            if isCon > 3:
                isCon=0
                enemy_x=width
                enemy_y = random.randrange(0, height-en_y)
                isShot = False
        if len(bullet_xy)!=0:
            for bx,by in bullet_xy:
                drawobj(bullet,bx,by)
        pg.display.flip()
        fps.tick(30)

def main():
    pg.init()
    global game,fps
    global player,backgr,backgr2
    global enemy,bullet,boom

    game = pg.display.set_mode((size))
    pg.display.set_caption('Shooting')
    fps = pg.time.Clock()

    player = pg.image.load('../img/plane.png')
    player = pg.transform.scale(player,(130,70))

    backgr = pg.image.load('../img/sky.png')
    backgr2 = backgr.copy()

    enemy = pg.image.load('../img/enemy.png')
    enemy = pg.transform.flip(enemy,1,0)
    enemy= pg.transform.scale(enemy,(150, 90))

    bullet = pg.image.load('../img/bullet.png')
    bullet = pg.transform.rotate(bullet,180)
    bullet = pg.transform.scale(bullet, (50,10))

    boom = pg.image.load('../img/boom.png')
    boom = pg.transform.scale(boom,(50,50))

    run()

main()