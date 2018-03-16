import numpy as np
from Constants import *

# CV = carrier
# BB = battleship
# CA = cruiser
# DD = destroyer
# OR = oil rig

class Ship(object):
    appendix = 'None'
    orientation = Orientation.VERTICAL
    shape = []
    placedLocation = []

    def __init__(self):
         super(Ship, self).__init__()
         self.orientation = self.randomPickOrientation()

    def getAppendix(self):
        return self.appendix

    def randomPickOrientation(self):
        random = np.random.random_integers(0,1)
        if random == 0:
            print('Vertical')
            return Orientation.VERTICAL
        print('Horizontal')
        return Orientation.HORIZONTAL

    def getNormalCoordinates(self):
        return self.shape

    def getPlacedCoordinates(self):
        return self.placedLocation + self.shape

    def getTransposedArray(self):
        numpyArray = np.array(self.shape)
        return np.flip(np.transpose(numpyArray), 0)

class Carrier(Ship):
    appendix = 'CV'

    def __init__(self):
        Ship.__init__(self)

    def initShape(self):
        if self.orientation == Orientation.VERTICAL:
            pass
        else:
            pass

class Battleship(Ship):
    appendix = 'BB'

    def __init__(self):
        Ship.__init__(self)

    def initShape(self):
        if self.orientation == Orientation.VERTICAL:
            pass
        else:
            pass

class Cruiser(Ship):
    appendix = 'CA'

    def __init__(self):
        Ship.__init__(self)

    def initShape(self):
        if self.orientation == Orientation.VERTICAL:
            pass
        else:
            pass

class Destroyer(Ship):
    appendix = 'DD'

    def __init__(self):
        Ship.__init__(self)
        self.initShape()

    def initShape(self):
        if self.orientation == Orientation.VERTICAL:
            self.shape = [[0, 0], [0, 1], [0, 2]]
        else:
            self.shape = [[0, 0], [1, 0], [2, 0]]

class OilRig(Ship):
    appendix = 'OR'

    def __init__(self):
        Ship.__init__(self)

    def initShape(self):
        if self.orientation == Orientation.VERTICAL:
            pass
        else:
            pass
