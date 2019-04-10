
BASE_SIZE = 3
BLANK_SPACE = ""
COLOUR_KEY = "colour"
PIECES_KEY = "pieces"
BLOCKS_KEY = "blocks"
BLOCKS_STR = "[=]"

import Formatting

board_dict = {}
#colour = ""

#give board own dictionary to store board state. set empty board
def init():
    # the dictionary to store these in
    coord_range = range(-BASE_SIZE, BASE_SIZE)
    # create board like in search.py
    for coord in [(q,r) for q in coord_range for r in coord_range if -q-r in coord_range]:
        board_dict[coord] = BLANK_SPACE

# initialises board based on json data
def setup(jsondata):
    init()
    print(jsondata.keys())
    colour = jsondata.pop(COLOUR_KEY)
    # read through file, add corresponding values to dictionary
    for key in jsondata.keys():
        for i in jsondata[key]:
            assign_to_board(key, tuple(i), colour)

# takes a key-value pair from json and adds it to board dictionary    
def assign_to_board(key, value, colour):
    
    # sets each coordinate value to current colour
    if key==PIECES_KEY:
        board_dict[value]=colour
    # sets each coord value to block
    elif key==BLOCKS_KEY:
        board_dict[value]=BLOCKS_STR

#TODO????? defunct with get_col_coord_dict???
def get_col_coord_tuple(colour):
        return tuple([Formatting.convert(coord) for coord in board_dict if board_dict[coord] == colour])

# returns a dictionary, with coordinates as keys and piece colour as values. so like up to four items.
def get_col_coord_dict(colour):
        #init new dictionary
        new_dict = {}
        for coord in board_dict:
                if board_dict[coord] == colour:
                        new_dict[Formatting.convert(coord)]=colour
        return new_dict

    

def get_board():
    return board_dict