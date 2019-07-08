import pygame
import sys

white = (255,255,255)

size = [800, 600]

class MAZE:

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(size)
        pygame.display.set_caption('maze')
        self.fps = pygame.time.Clock()
        self.width = 800
        self.height = 600

    def maze(self):
        maze_x = 17
        maze_y = 11
        make_maze=[[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                       [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                       [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
                       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        start_point = (0, 1)
        end_point = (16, 10)

        mx =0
        my =0
        for i in range(0,maze_x*maze_y):
            if make_maze[my][mx] ==1:
                pygame.draw.rect(self.display, white, (mx*20, my*20, 20, 20),1)
            mx +=1
            if mx == maze_x:
                mx=0
                my+=1
    def move(self):
        key=pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            pass
        elif key[pygame.K_LEFT]:
            pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.maze()
            pygame.display.flip()

if __name__=="__main__":
    MAZE().run()