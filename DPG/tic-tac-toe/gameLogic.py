import numpy as np
from utils import check_consecutive


class GameLogic():

    def __init__(self):

        # -1: blank
        #  0: 'O'
        #  1: X
        
        # initial state of the board
        self.state = np.array([
            [-1,-1,-1],
            [-1,-1,-1],
            [-1,-1,-1]
        ])
        
        self.is_win = False
        self.winner = None

        self.players ={
            "player_1":1,
            "player_2":0
        }
   
    def execute_move(self, position, mode):
        row, col = position
        if self.possible_move(position):
            self.state[row, col] = mode

    def possible_move(self, position):
        row, col = position
        if self.state[row,col] == -1:
            return True
        return False

    # Function that checks if a win state happens
    # return True/winner or False/None
    def is_win(self):
        if check_consecutive(self.state, 0, 3):
            return True, 0
        
        if check_consecutive(self.state, 1, 3): 
            return True, 1
        
        return False, None
    
    # Function to return all the numpy arrays of possible states
    def possible_states(self):
        pass


    def minimax(self):
        root_node = Node(self.state)


class Node:
    
    def __init__(self, gameLogic): 
        self.state = gameLogic.state
        self.value = self.evaluate(self.state)
        

    def generate_childs(sefl):  
        pass

    def evaluate(self, player, state):
        pass


        