from textx import metamodel_from_str, get_children_of_type
import numpy as np
import random

grammar = """
Model: commands*=GameCommand;
GameCommand: MoveCommand | ActionCommand;
MoveCommand: Left|Right|Up|Down;
ActionCommand: Reset | Exit;
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

def command_validator(model, finish, player, stop, game, size):
	for command in model.commands:
		_cname = cname(command)
		delta = 1 if command.count == 0 else command.count
		if _cname == 'Left' and player.x - delta >= 0 :
			player.x = player.x - delta
		elif _cname == 'Right' and player.x + delta <= size - 1:
			player.x = player.x + delta
		elif _cname == 'Up' and player.y - delta >= 0:
			player.y = player.y - delta
		elif _cname == 'Down' and player.y + delta <= size -1:
			player.y = player.y + delta
		else:
			if command == 'reset':
				game, finish, player = create_game(board_size)
			elif command == 'exit':
				print("Exiting...")
				stop = True
				
	game = np.zeros((board_size, board_size))
	game[player.y][player.x] = '1'
	game[finish.y][finish.x] = '2'
	if player.x == finish.x and player.y == finish.y:
		stop = True
		print("Victory!")
	return finish, player, stop, game

def create_game(board_size):
	game = np.zeros((board_size, board_size))
	finish = Coordinate(random.randint(0, board_size-1), random.randint(0, board_size-1))
	player = Coordinate(random.randint(0, board_size-1), random.randint(0, board_size-1))
	game[player.y][player.x] = '1'
	game[finish.y][finish.x] = '2'
	return game, finish, player

mm = metamodel_from_str(grammar)

board_size = 10

game, finish, player = create_game(board_size)

stop = False

while not stop:
	print(game)
	print("\nMove single cell: '<left, right, up, down>'")
	print("Move multiple cells: '<left, right, up, down> XCELLS'")
	print("Reset game: 'reset'")
	print("Exit game: 'exit'")
	command = input('Enter command: ')
	finish, player, stop, game = command_validator(mm.model_from_str(command), finish, player, stop, game, board_size)