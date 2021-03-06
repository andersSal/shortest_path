
#  Code similar to astar.grid.py with the exception of:
#  - No f, g or cost-values

class Node:
    def __init__(self, row: int, col: int , char: chr):
        '''

       :param int row: index of row
       :param int col: index of col
       :param str char: character in node

       '''
        self.row = row
        self.col = col
        self.char = char
        self.status = None  # open, closed or path


class Board:
    def __init__(self, path: str):
        '''

       Initializes a matrix of Nodes
       :param str path: path of board.txt

       '''
        file = open(path, 'r')
        lines = file.read().split()
        self.num_rows = len(lines)
        self.num_cols = len(lines[0])
        self.matrix = [[[0] for _ in range(self.num_cols)] for _ in range(self.num_rows)]  # Initializing empty matrix
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                char = lines[i][j]
                if char == 'A':
                    self.start_coordinates = (i, j)
                elif char == 'B':
                    self.goal_coordinates = (i, j)
                self.matrix[i][j] = Node(i, j, char)

    def get_children(self, node):
        '''

        :param Node node: current node
        :return: list of children/neighbor nodes

        '''
        children = []
        row = node.row
        col = node.col
        if col + 1 < self.num_cols and self.matrix[row][col + 1].char != '#':
            children.append(self.matrix[row][col + 1])
        if col - 1 >= 0 and self.matrix[row][col - 1].char != '#':
            children.append(self.matrix[row][col - 1])
        if row + 1 < self.num_rows and self.matrix[row + 1][col].char != '#':
            children.append(self.matrix[row + 1][col])
        if row - 1 >= 0 and self.matrix[row - 1][col].char != '#':
            children.append(self.matrix[row-1][col])
        return children

    # Unused
    def __str__(self):  # Not used (Print result-board to console)
        s = ' ' + '_' * self.num_cols + '\n|'
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                node = self.matrix[i][j]
                if node.char == 'A':
                    s += 'A'
                elif node.char == 'B':
                    s += 'B'
                elif node.status == 'path':
                    s += 'o'
                elif node.status == 'closed':
                    s += 'x'
                elif node.status == 'open':
                    s += '*'
                else:
                    s += node.char
            s += "|\n|"
        s = s[:-1] + ' ' + '-' * (self.num_cols + 1)
        return s[:-1]



