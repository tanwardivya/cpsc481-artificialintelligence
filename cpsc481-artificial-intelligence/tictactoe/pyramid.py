from aima_python.games import *

class Pyramid(TicTacToe):
    """Play Pyramid TicTacToe, with Max (first player) playing 'X'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a dict of {(x, y): Player} entries, where Player is 'X' or 'O'."""
    def __init__(self, h=3, v=5, k=3):
        self.h = h
        self.v = v
        self.k = k
        moves = []
        start = 1
        end = v+1
        for x in range(1,h+1):
            for y in range(start,end):
                moves.append((x,y))
            start= start +1
            end = end - 1
        self.possible_moves = moves
        self.weights={}
        weight =1 
        mid = int(len(moves)/2) - 1
        for index in range(0, len(moves)):
            if index <= mid:
                self.weights[moves[index]] = weight
                weight+=1
            else:
                self.weights[moves[index]] = weight
                weight= weight -1
                
        self.initial = GameState(to_move='X', utility=0, board={}, moves=moves)
          
    def display(self, state):
        board = state.board
        for x in range(self.h , 0, -1):
            for y in range(1, self.v+1):
                if (x,y) in self.possible_moves:
                    print(board.get((x, y), '.'), end=' ')
                else:
                    print(end='  ')
            print()
    
    def compute_utility(self, board, move, player):
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."""
        
        if (self.k_in_row(board, move, player, (0, 1)) or
                self.k_in_row(board, move, player, (1, 0)) or
                self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return +1*self.weights[move] if player == 'X' else -1*self.weights[move]
        else:
            return 0



if __name__ == "__main__":
    pyramid = Pyramid() # Creating the game instance
    print(pyramid.initial.moves) # must be [(1,1), (1,2), (1,3), (1,4), ...]
    utility = pyramid.play_game(minmax_player, query_player) # computer moves first
    if (utility == 0):
        print("TIED game")
    elif (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
