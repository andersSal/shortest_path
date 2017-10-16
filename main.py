import os
from astar import astar as a, grid as a_grid
from dijkstra import dijkstra as d, grid as d_grid
from bfs import bfs as b, grid as b_grid
from img import get_image


def run_all(directory: str, show: bool):

    '''

    Runs all boards in directory with all algorithms. Saves the result-images in the results folder in current directory
    :param str directory: The path to the directory of boards-folder with .txt-files.
    :param bool show: Whether or not you want the results to pop up...

    '''

    save_location = os.path.dirname(os.path.realpath(__file__)) + "/results"
    if not directory.endswith('/'):
        directory += '/'

    if not os.path.exists(save_location):
        # Creates sub-folders for each algorithm
        os.makedirs(save_location + "/astar")
        os.makedirs(save_location + "/dijkstra")
        os.makedirs(save_location + "/bfs")

    for filename in os.listdir(directory):
        save_a = save_location + "/astar/"
        board = a_grid.Board(directory + filename)
        start = board.matrix[board.start_coordinates[0]][board.start_coordinates[1]]
        goal = board.matrix[board.goal_coordinates[0]][board.goal_coordinates[1]]
        a.astar(start, goal, board)
        image = get_image(board)
        image.save(save_a + filename[:-4] + '.jpeg', 'JPEG')

        save_d = save_location + "/dijkstra/"

        board = d_grid.Board(directory + filename)
        start = board.matrix[board.start_coordinates[0]][board.start_coordinates[1]]
        goal = board.matrix[board.goal_coordinates[0]][board.goal_coordinates[1]]
        d.shortest_path(start, goal, board)
        image = get_image(board)
        image.save(save_d + filename[:-4] + '.jpeg', 'JPEG')

        save_b = save_location + "/bfs/"
        board = b_grid.Board(directory + filename)
        start = board.matrix[board.start_coordinates[0]][board.start_coordinates[1]]
        goal = board.matrix[board.goal_coordinates[0]][board.goal_coordinates[1]]
        b.shortest_path(start, goal, board)
        image = get_image(board)
        image.save(save_b + filename[:-4] + '.jpeg', 'JPEG')
        if show:
            image.show()


def run_one_board(board_path: str, algorithm: str):

    '''

    Runs one board with the specified algorithm, displays the result
    :param str board_path: The path to the .txt-file you want to run.
    :param str algorithm: Either: 'astar', 'dijkstra', 'bfs'

    '''

    if algorithm == 'astar':
        board = a_grid.Board(board_path)
        start = board.matrix[board.start_coordinates[0]][board.start_coordinates[1]]
        goal = board.matrix[board.goal_coordinates[0]][board.goal_coordinates[1]]
        a.astar(start, goal, board)
        image = get_image(board)
    elif algorithm == 'bfs':
        board = b_grid.Board(board_path)
        start = board.matrix[board.start_coordinates[0]][board.start_coordinates[1]]
        goal = board.matrix[board.goal_coordinates[0]][board.goal_coordinates[1]]
        b.shortest_path(start, goal, board)
        image = get_image(board)
    else:
        board = d_grid.Board(board_path)
        start = board.matrix[board.start_coordinates[0]][board.start_coordinates[1]]
        goal = board.matrix[board.goal_coordinates[0]][board.goal_coordinates[1]]
        d.shortest_path(start, goal, board)
        image = get_image(board)
    image.show()


def run():
    '''

    Example of use:
    1. run_all('User/.../boards/', True)
    2. run_one_board('User/.../boards/board-1-1-txt', 'astar')

    '''
    run_one_board('/Users/anderssalvesen/PycharmProjects/IntroAI/A_star/boards/board-1-1.txt', 'astar')

run()
