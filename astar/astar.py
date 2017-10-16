import heapq
from astar import grid


def astar(start: grid.Node, goal: grid.Node, board: grid.Board):
    '''

    :param grid.Node start: Start node
    :param grid.Node goal: Goal Node
    :param grid.Board board:
    :return: Success --> a grid.Board, Failure: str

    '''
    open_list = []                         # -> implemented as a min-priority-queue using heapq
    heapq.heappush(open_list, start)       # -> Add first node to open_list
    parents = {}                           # -> dict with nodes to update best parent
    start.g = 0                            # -> set distance to root node to 0
    start.f = calc_heuristic(start, goal)  # -> Root node's f is only the heuristic

    while open_list:
        heapq.heapify(open_list)
        current = heapq.heappop(open_list)  # get the most promising node
        if (current.row, current.col) == (goal.row, goal.col):  # path found
            return reconstruct_path(parents, current, board)  # start traceback via parents dict
        current.status = 'closed'  # marks node as closed (Using Node.status-variable instead of closed-list)
        children = board.get_children(current)
        for child in children:
            if child.status == 'closed':
                continue  # ignore node which has already been evaluated
            if child not in open_list:
                open_list.append(child)  # new node is discovered, add to open_list
                child.status = 'open'  # marked as open for visualization purposes
            new_g = current.g + child.cost
            if new_g >= child.g:
                continue  # path is worse, move on to next child
            parents[child] = current  # found a better path, update parent, g- and f-values
            child.g = new_g
            child.f = new_g + calc_heuristic(child, goal)
    return "Failed, no solution found"


def calc_heuristic(start: grid.Node, goal: grid.Node):  # Calculates manhattan distance
    return abs(start.row - goal.row) + abs(start.col - goal.col)


def reconstruct_path(parents: dict, current: grid.Node, board: grid.Board):
    while current in parents.keys():
        current = parents[current]  # Trace back parents from goal node
        if (current.row, current.col) != board.start_coordinates:
            current.status = 'path'  # node marked as path for visualization purposes
    return board
