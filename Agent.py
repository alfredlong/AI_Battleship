import numpy as np

class Agent(object):
    def __init__(self, selfBoard, enemyBoard):
        super(Agent, self).__init__()
        self.selfBoard = selfBoard
        self.enemyBoard = enemyBoard

    def tryPlaceShip(self, location, ship, color):
        print('Color: ' + str(color))
        print('Location: ' + str(location))
        rs_location = np.reshape(location,(2,1))
        idx = zip(rs_location+ship)
        if self.selfBoard.checkGrid[idx].all() and not self.selfBoard.dataGrid[idx].any():
            self.selfBoard.dataGrid[idx] = color
            print('Status: Success')
            return True
        print('Status: Fail')
        return False

    def placeShips(self, ships):
        for ship in ships:
            location = self.pickRandomSpot()
            while self.tryPlaceShip(location, ship[0], ship[1]) == False:
                location = self.pickRandomSpot()

    def pickRandomSpot(self):
        return (np.random.random_integers(0,self.selfBoard.rowsNum-1), np.random.random_integers(0,self.selfBoard.colsNum-1))
