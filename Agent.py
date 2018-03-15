import numpy as np
from Constants import *

class Agent(object):
    potentialTargetList = []
    fightMode = FightMode.HUNT
    shotCount = 0

    def __init__(self, selfBoard, enemyBoard):
        super(Agent, self).__init__()
        self.selfBoard = selfBoard
        self.enemyBoard = enemyBoard

    def tryPlaceShip(self, location, ship, color):
        print('Color: ' + str(color))
        print('Location: ' + str(location))

        rs_location = np.reshape((location[1], location[0]),(2,1))
        idx = zip(rs_location+ship)
        if self.selfBoard.checkGrid[idx].all() and not self.selfBoard.dataGrid[idx].any():
            self.selfBoard.dataGrid[idx] = color
            print('Status: Success')
            return True
        print('Status: Fail')
        return False

    def placeShips(self, ships):
        for ship in ships:
            location = self.pickRandomSpot(self.selfBoard)
            while self.tryPlaceShip(location, ship[0], ship[1]) == False:
                location = self.pickRandomSpot(self.selfBoard)

    def pickRandomSpot(self, board):
        return (np.random.random_integers(0, board.n_x-1), np.random.random_integers(0, board.n_y-1))

    def huntShip(self):
        pickedX, pickedY = self.pickRandomSpot(self.enemyBoard)
        while self.checkValidCell(pickedX, pickedY, self.enemyBoard) == False:
            pickedX, pickedY = self.pickRandomSpot(self.enemyBoard)
        result = self.shotBoard(pickedX, pickedY)
        if result == SeaState['HIT']:
            self.fightMode = FightMode.TARGET
            self.findAndAddPotentialTargetsToList(pickedX, pickedY, self.enemyBoard)
        self.enemyBoard.updateCell(pickedX, pickedY, result)

    def targetShip(self):
        if len(self.potentialTargetList) > 0:
            nextX, nextY = self.potentialTargetList.pop()
            result = self.shotBoard(nextX, nextY)
            if result == SeaState['HIT']:
                self.findAndAddPotentialTargetsToList(nextX, nextY, self.enemyBoard)
            self.enemyBoard.updateCell(nextX, nextY, result)
        else:
            self.fightMode = FightMode.HUNT
            self.huntShip()


    def shotBoard(self, x, y):
        # DUMMY
        self.shotCount += 1
        if self.enemyBoard.dataGrid[int(y)][int(x)] == SeaState['CLEAR']:
            return SeaState['MISS']
        else:
            return SeaState['HIT']

    def checkValidCell(self, x, y, board):
        if x < 0 or x > board.n_x - 1:
            return False
        if y < 0 or y > board.n_y - 1:
            return False
        if board.dataGrid[int(y)][int(x)] != SeaState['CLEAR'] and board.dataGrid[int(y)][int(x)] < 10: # TEMP
            return False
        return True

    def findAndAddPotentialTargetsToList(self, startX, startY, board):
        deltaX = [0, 0, 1, -1]
        deltaY = [1, -1, 0, 0]

        # Add potential point to stack
        for i in xrange(4):
            newX = startX + deltaX[i]
            newY = startY + deltaY[i]

            if self.checkValidCell(newX, newY, board):
                self.potentialTargetList.append((newX, newY))
