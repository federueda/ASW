from textx import metamodel_from_str, get_children_of_type
import numpy as np
import random

grammar = """
Left: 'left' count=INT?;
Right: 'right' count=INT?;
Up: 'up' count=INT?;
Down: 'down' count=INT?;
Reset: 'reset';
Exit: 'exit';
"""

def cname(o):
    return o.__class__.__name__

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{},{}".format(self.x, self.y)

def command_validator(command):
    print(command.count)

mm = metamodel_from_str(grammar)

board_size = 10

game = np.zeros((board_size, board_size))

finish = Coordinate(random.randint(0, board_size-1), random.randint(0, board_size-1))
player = Coordinate(random.randint(0, board_size-1), random.randint(0, board_size-1))

finish = Coordinate(1,5)
player = Coordinate(1,1)

stop = False

while not stop:
    print(game)
    print("\nMove single cell: '<left, right, up, down>'")
    print("Move multiple cells: 'move to <left, right, up, down> XCELLS'")
    print("Reset game: 'reset'")
    print("Exit game: 'exit'")
    command = input('Enter command: ')
    model_str = """
    left
    """
    command_validator(mm.model_from_str(model_str))