import numpy as np
import matplotlib.pyplot as plt
from Board import Board
from Agent import Agent

n_rows = 10
n_cols = 20

# Define some ships
battleship = np.array([[0,1,2,3],[0,0,0,0]])
patrol = np.array([[0,1],[0,0]])
uboat  = np.array([[0,0,1,2,2],[1,0,0,0,1]])
carrier = np.array([[0,1,1,2,3],[0,0,1,0,0]])
carrier_v = np.array([[0,1,0,0,0],[0,1,1,2,3]])
v_idx = [1,0]

shipsArray = [(patrol, 1), (battleship, 2), (battleship[v_idx], 2), (uboat, 3), (carrier, 4), (carrier_v, 4)]

gameBoard = Board(n_rows, n_cols)
agent = Agent(gameBoard, None)

agent.placeShips(shipsArray)
gameBoard.drawBoard()

x = raw_input("X: ")
y = raw_input("Y: ")

gameBoard.updateCell(x, y, 5)

x = raw_input("X: ")
y = raw_input("Y: ")

gameBoard.updateCell(x, y, 5)

x = raw_input("X: ")
y = raw_input("Y: ")
