from gridview import GridView
from random_maze import RandomMaze
import A_star_logic
from time import sleep

# from path_finder import MazePathFinder

import pygame
import sys

pygame.init()

DFS = 1
Kruskal = 2

width = 984
height = 504
grid_size = 24

background_color = (230, 230, 100)
grid_line_color = (0, 0, 0)
cell_color = (50, 50, 255)
path_color = (255, 50, 50)

resolution = (width, height)

start_point=(2,1)
end_point=((height//grid_size-3),(width//grid_size)-2)

ran_maze = RandomMaze(width // grid_size, height // grid_size)

def get_maze_method(option):  # 선택 값에 따른 알고리즘으로 미로 제작
    if option == 1:
        return ran_maze.dfs_maze
    elif option == 2:
        return ran_maze.disjoint_make_maze
    else:
        return None


def main(maze_method, speed=0.010, mode=0):
    check =0
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("A_star_Maze")
    #pygame.display.set_icon(pygame.image.load(""))
    clock = pygame.time.Clock()
    maze, cell_list = maze_method()  # 랜덤으로 생성된 2차원 리스트 미로와 xxx 좌표가 담긴 리스트를 받는다

    path = A_star_logic.main(maze,start_point,end_point)
    index = 0
    maze_finished = False

    pass_time = 0
    grid_view = GridView(screen, width, height, grid_size, grid_line_color)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        press_key = pygame.key.get_pressed()

        # press F5 to regenerate the maze
        if press_key[pygame.K_F5]:
            index = 0
            # path_index = 0
            maze, cell_list = maze_method()
            path = A_star_logic.main(maze, start_point, end_point)
            maze_finished = False
            check=0
        elif press_key[pygame.K_d]:
            main(maze_method=get_maze_method(DFS), mode=1)
            pass
        elif press_key[pygame.K_k]:
            main(maze_method=get_maze_method(Kruskal), mode=1)

        # print index

        if mode == 0:
            screen.fill(background_color)
        else:
            screen.fill(cell_color)

        # draw the cell
        for i in range(index + 1):
            if mode == 0:
                grid_view.fill_a_cell(cell_list[i][1], cell_list[i][0], cell_color)
            else:
                grid_view.fill_a_cell(cell_list[i][1], cell_list[i][0], background_color)

        # draw the grid
        grid_view.draw()

        # draw the path
        if maze_finished and path:
                for i in range(len(path)):
                    grid_view.fill_a_cell_with_circle(path[i][1], path[i][0], path_color)
                    pygame.display.update()
                    sleep(0.1)
                maze_finished=False
                check=1

        time_passed_seconds = clock.tick() / 1000.0
        pass_time += time_passed_seconds

        if pass_time >= speed:
            pass_time = 0

            if index >= len(cell_list) - 1 and check==0:
                    maze_finished = True
                    print("랜덤으로 생성된 미로 탐색 비용은 : "+str(len(path)))

            if index + 1 < len(cell_list):
                index += 1
                pygame.display.update()


'''def parser_arg(argv):
        """
        parser the arguments,
        python main.py [OPTION]:
                -d --dfs: use dfs algorithm to generate the maze, and return 1(default value)
                -k --kruscal: use kruscal algorithm to generate the maze, and return 2
        """
        args = argv[1:]
        if len(args) == 0:
                return 1
        elif len(args) > 1:
                print 'Error option'
                print 'Usage:'
                print "(python) main.py [OPTION]: \n" + \
                "  -d --dfs: use dfs algorithm to generate the maze(default option)\n" +\
                "  -k --kruscal: use kruscal algorithm to generate the maze "
                return 0
        elif args[0] == '-d' or args[0] == '--dfs':
                return 1
        elif args[0] == '-k' or args[0] == '--kruscal':
                return 2
        else:
                print 'Error option'
                print 'Usage:'
                print "(python) main.py [OPTION]: \n" + \
                "  -d --dfs: use dfs algorithm to generate the maze(default option)\n" +\
                "  -k --kruscal: use kruscal algorithm to generate the maze "
                return 0'''

if __name__ == '__main__':

    method = get_maze_method(DFS)  # 미로를 제작할 알고리즘 선택

    if method:
        main(maze_method=method, mode=1)
    else:
        print("미로를 제작할 값이 올바르지 않습니다.")
