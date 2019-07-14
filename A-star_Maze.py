import pygame
import sys
from time import sleep
import tkinter

white = (255,255,255)
gold = (255,204,0)
green = (0,255,0)
dark_green=(0,153,0)
black = (0, 0, 0)

size = [800, 600]
box_size = 45 # setup box size
player_size = 20 # setup player size

start_point = (0, 1)  # start x,y
end_point = (15, 9)  # end x,y

maze_x = 17  # max maze x
maze_y = 11  # max maze y

make_maze=[[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
           [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
           [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

class MAZE:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(size) # display setup
        pygame.display.set_caption('maze') # caption setup
        pygame.display.set_icon(pygame.image.load('img/maze.png')) # icon setup
        self.fps = pygame.time.Clock() # fps setup

        self.player_x = 70 # pixcel x
        self.player_y = 20 # pixecl y

        self.x = start_point[1] # real x
        self.y = start_point[0] # real y

        self.check = 0

        self.font = pygame.font.SysFont("Century", 40) # font setup

        self.maze()

    def maze(self):
        pygame.draw.rect(self.display, gold, (end_point[0] * box_size, end_point[1] * box_size, box_size, box_size))

        #draw maze
        mx = 0
        my = 0
        for i in range(0,maze_x*maze_y):
            if make_maze[my][mx] ==1:
                pygame.draw.rect(self.display, white, (mx*box_size, my*box_size, box_size, box_size),2)
            mx +=1
            if mx == maze_x:
                mx=0
                my+=1

    def char(self):
        self.player = pygame.Rect(self.player_x,self.player_y,player_size,player_size) # character setup

    def move(self):
        key=pygame.key.get_pressed()
        speed = 0.3

        if key[pygame.K_RIGHT]: # move right
            if make_maze[self.y][self.x + 1] == 1:
                pass
            elif make_maze[self.y][self.x + 1]==2:
                pass
            else:
                self.player_x += box_size
                self.x+=1
                self.check+=1
                make_maze[self.y][self.x]=2;
                sleep(speed)

        elif key[pygame.K_LEFT]: # move left
            if make_maze[self.y][self.x - 1] == 1:
                pass
            elif make_maze[self.y][self.x - 1] == 2:
                pass
            else:
                self.player_x -= box_size
                self.x-=1
                self.check += 1
                make_maze[self.y][self.x] = 2;
                sleep(speed)

        elif key[pygame.K_UP]: # move up
            if make_maze[self.y-1][self.x] == 1:
                pass
            elif make_maze[self.y-1][self.x] == 2:
                pass
            else:
                self.player_y -= box_size
                self.y-=1
                self.check += 1
                make_maze[self.y][self.x] = 2;
                sleep(speed)

        elif key[pygame.K_DOWN]: # move down
            if make_maze[self.y+1][self.x] == 1:
                pass
            elif make_maze[self.y+1][self.x] == 2:
                pass
            else:
                self.player_y += box_size
                self.y+=1
                self.check += 1
                make_maze[self.y][self.x] = 2;
                sleep(speed)

    def show(self):
        if self.font:
            font_surface = self.font.render("Count: " + str(self.check), True, white)
            self.display.blit(font_surface, (600, 500))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.fps.tick(30)
            self.display.fill(black)

            self.move()
            self.maze()
            self.char()

            pygame.draw.circle(self.display,green,(self.player.left,self.player.top),player_size) # draw character
            pygame.draw.circle(self.display, dark_green, (self.player.left-1, self.player.top-1), player_size)  # draw gradation

            self.show()
            pygame.display.flip()


            if self.x == end_point[0] and self.y == end_point[1]:
                print("목적지에 도착!\n도착까지의 비용은 : "+str(self.check))
                pygame.quit()
                sys.exit()

if __name__=="__main__": # start main
    MAZE().run()
