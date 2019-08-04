class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent  # 부모 노드
        self.position = position  # 노드 위치

        # 노드의 g,h,f
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
    start_node = Node(None, start)  # 시작 노드 생성
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)  # 도착 노드 생성
    end_node.g = end_node.h = end_node.f = 0

    open_list = []  # 오픈 리스트
    closed_list = []  # 닫힌 리스트

    open_list.append(start_node)  # 오픈 리스트 처음은 시작 노드 값으로

    while len(open_list) > 0:  # 오픈 리스트에 노드가 없을때 종료
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):  # 오픈 리스트 노드들중에 가장 최소 비용 F를 가진 노드를 찾는다
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)  # 오픈 리스트에 해당하는 노드 pop
        closed_list.append(current_node)  # 닫힌 리스트에 해당 노드 input

        if current_node == end_node:  # 도착 노드까지 탐색이 완료될 경우
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # 역순으로 출력되게 반전 상태로 리턴 시킨다

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 동서남북 그리고 대각선 방향으로 한칸씩 이동

            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 \
                    or node_position[1] > (len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:  # 이동될 지점이 maze 바깥일때
                continue

            if maze[node_position[0]][node_position[1]] == 1:  # 이동될 지점이 벽일때
                continue
            elif node_position[1]==start[1]-1 and current_node.position==start_node.position:
                continue


            new_node = Node(current_node, node_position)

            children.append(new_node)  # 자식 노드에 이동할 지점 즉 이동 노드 값 대입

        for child in children:
            check = False
            for closed_child in closed_list:
                if child == closed_child:  # 탐색중인 자식 노드가 닫힌 리스트와 같은 값일 경우
                    check = True

            if check == False:
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[1]) ** 2) + (
                            (child.position[1] - end_node.position[0]) ** 2)  # 수평방향은 10, 대각선은 12
                child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                open_list.append(child)

def main(maze,start,end):
    path = astar(maze, start, end)  # a star 탐색 결과
    return path
    #print("도착지까지의 최소 경로는 : ", path)  # 경로 출력
    #print("경로에 드는 비용은 : ", len(path))  # 최소 비용 출력