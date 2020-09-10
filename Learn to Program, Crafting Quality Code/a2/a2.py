# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    
    def __init__(self, symbol, row, col):
        """
        (Rat, str, int, int) -> NoneType
        """
        
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """
        (Rat, int, int) -> NoneType
        """

        self.row = row
        self.col = col

    def eat_sprout(self):
        """
        (Rat) -> NoneType
        """

        self.num_sprouts_eaten = self.num_sprouts_eaten + 1

    def __str__(self):
        """
        (Rat) -> NoneType
        """

        return '{0} at ({1},{2}) ate {3} sprouts'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.

    def __init__(self, maze, rat_1, rat_2):
        """
        (Maze, list of list of str, Rat, Rat) -> NoneType
        """

        num_sprouts_left = 0

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        self.maze[rat_1.row][rat_1.col] = rat_1.symbol
        self.maze[rat_2.row][rat_2.col] = rat_2.symbol

        for row in maze:
            for char in row:
                if char == '@':
                    num_sprouts_left = num_sprouts_left + 1

        self.num_sprouts_left = num_sprouts_left
        

    def is_wall(self, row, col):
        """
        (Maze, int, int) -> NoneType
        """

        return self.get_character(row,col) == WALL

    def get_character(self, row, col):
        """
        (Maze, int, int) -> NoneType
        """

        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol
        elif self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]

    def move(self, rat, row, col):
        """
        (Maze, Rat, int, int) -> NoneType
        """

        row = rat.row + row
        col = rat.col + col
        if self.is_wall(row, col)!= True:
            if self.get_character(row, col) =='@':
                self.maze[row][col] = '.'
                self.num_sprouts_left = self.num_sprouts_left - 1
                self.num_sprouts_eaten = rat.num_sprouts_eaten + 1
            rat.row = row
            rat.col = col
            return True
        

    def __str__(self):
        """
        (Maze) -> str
        """

        result = ''
        for row in self.maze:
            for i in row:
                result = result + i
            result = result + '\n'
        return result + '{0}\n{1}'.format(self.rat_1, self.rat_2)
