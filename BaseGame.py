import numpy as np
import matplotlib.pyplot as plt
from Board import Board
from Agent import Agent
from Ship import *
from Constants import *

n_x = 20
n_y = 8

# Define some ships
# battleship = np.array([[0,1,2,3],[0,0,0,0]])
# patrol = np.array([[0,1],[0,0]])
# uboat  = np.array([[0,0,1,2,2],[1,0,0,0,1]])
# carrier = np.array([[0,1,1,2,3],[0,0,1,0,0]])
# carrier_v = np.array([[0,1,0,0,0],[0,1,1,2,3]])
# v_idx = [1,0]

# shipsArray = [(patrol, 11), (battleship, 12), (battleship[v_idx], 12), (uboat, 13), (carrier, 14), (carrier_v, 14)]

destroyer = Destroyer()
shipsArray = [(destroyer, 11)]

gameBoard = Board(n_x, n_y)
agent = Agent(gameBoard, gameBoard)

agent.placeShips(shipsArray)
gameBoard.drawBoard()

# while np.count_nonzero(gameBoard.dataGrid > 10) > 0:
#     if agent.fightMode == FightMode.HUNT:
#         agent.huntShip()
#     else:
#         agent.targetShip()
#
# print('Total shots: ' + str(agent.shotCount))

raw_input()
