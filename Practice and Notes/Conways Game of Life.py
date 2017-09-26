import numpy as np
from numpy.random import choice
#
## user input (width, height, ticks)
#WHN = (10,10,10)
#x = WHN[0]
#y = WHN[1]
#n = WHN[2]
#
#values = [-1,0,1]
#grid = [[random.choice(values) for row in xrange(WHN[0])] for column in xrange(WHN[1])]

class Game(object):
    def __init__(self, state, infinite_board=True):
        self.state = state
        self.width = state.width
        self.height = state.height
        self.infinite_board = infinite_board
        
    def step(self, count=1):
        for generation in range(count):
            
        
    def build_board(self):
#        values = ['o','.'] # on and off respectively
#        wts = [0.4, 0.6] # weight distribution
#        self.grid = [x[:] for x in [[choice(values, p=wts)] * self.w] * self.h] # create 2d grid
#              
#        for i in xrange(self.w):
#            for j in xrange(self.h):
#                self.grid[i][j].append(choice(values, p=wts)) # create 2d grid
    
    def count_nbr(self, x, y):
        count = 0
        prox = [-1,0,1]
        for hor in prox:
            for ver in prox: # don't go over the edge of the grid, don't check current cell
                if (not(hor == 0 and ver == 0) and (0 <= x + hor < self.w and 0 <= y + ver < self.h)):
                    count += 1
        print count
        
class State(object):
    def __init__(self, positions, x, y, width, height):
        
                
#test = Game(20,20,5)
#test.build_board()
#print test.grid
#print test.count_nbr(1,0)