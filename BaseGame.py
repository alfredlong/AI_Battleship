import numpy as np
import matplotlib.pyplot as plt
from Board import Board
from Agent import Agent
from Ship import *
from Constants import *

n_x = 20
n_y = 8

# Define ship amount
ownShips = {
    'CV': 2,
    'BB': 2,
    'OR': 2,
}
enemyShips = {
    'CV': 2,
    'BB': 2,
    'OR': 2,
}

# Define some ships
# carrier = Carrier()
# destroyer = Destroyer()
# battleship = Battleship()
# oilRig = OilRig()
# cruiser = Cruiser()
# shipsArray = [(destroyer, destroyer.shipId + 10), (oilRig, oilRig.shipId + 10), (carrier, carrier.shipId + 10), (battleship, battleship.shipId + 10), (cruiser, cruiser.shipId + 10)]

gameBoard = Board(n_x, n_y)
agent = Agent(gameBoard, gameBoard, ownShips, enemyShips)

agent.placeShips(agent.ownShipsArray)
gameBoard.drawBoard()

for ship in agent.ownShipsArray:
    print('Id: ' + str(ship[0].shipId))
    print('Position: ' + str(ship[0].getPlacedCoordinates()))
    print('Normal: ' + str(ship[0].getNormalCoordinates()))

while np.count_nonzero(gameBoard.dataGrid >= 10) > 0:
    if agent.fightMode == FightMode.HUNT:
        agent.huntShip()
    else:
        agent.targetShip()

print('Total shots: ' + str(agent.shotCount))

raw_input()
