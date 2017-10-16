from queue import *
from astar import grid
'''
    * Code is similar to astar.py with the exception these changes:
        - open_list is implemented as a FIFO-queue instead of a min-priority-queue
        - No f and g-values, and no cost-calculations
        - No heuristic calculations
    * BFS is guaranteed to find a shortest path if it exists, but this path
        will only be optimal with non-weighted edges
'''


def shortest_path(start: grid.Node, goal: grid.Node, board: grid.Board):
    '''

    :param grid.Node start: Start node
    :param grid.Node goal: Goal Node
    :param grid.Board board:
    :return: Success --> a grid.Board, Failure: str

    '''
    open_queue = Queue()        # -> implemented as a min-priority-queue using heapq
    open_list = []              # -> list to peek queue
    open_queue.put(start)       # -> put start node in open_queue
    open_list.append(start)     # -> and open list

    parents = {}

    while open_queue:
        current = open_queue.get()  # get first node in queue
        open_list.remove(current)
        if (current.row, current.col) == (goal.row, goal.col):  # path found
            return reconstruct_path(parents, current, board)
        current.status = 'closed'  # marks node as closed (Using Node.status-variable instead of closed-list)
        children = board.get_children(current)
        for child in children:
            if child.status == 'closed':
                continue  # ignore node which has already been evaluated
            if child not in open_list:
                open_queue.put(child) # new node is discovered, add to open_queue
                open_list.append(child)
                child.status = 'open'  # marks node as closed for visualization purposes)
            parents[child] = current  # found a better path, update parent, g and f-values
    return "Failed, no solution found"


def reconstruct_path(parents: dict, current: grid.Node, board: grid.Board):
    while current in parents.keys():
        current = parents[current]  # Trace back parents from goal node
        if (current.row, current.col) != board.start_coordinates:
            current.status = 'path'  # node marked as path for visualization purposes
    return board

