import numpy as np
import matplotlib.pyplot as plt
from Constants import *

class Board(object):
    dataGrid = np.zeros((0, 0))
    checkGrid = np.zeros((0, 0))
    maxShipLength = 5
    n_time = 1

    def __init__(self, rowsNum, colsNum):
        super(Board, self).__init__()
        self.rowsNum = rowsNum
        self.colsNum = colsNum
        self.initDataGrid();

    def initDataGrid(self):
        self.dataGrid = np.zeros((self.rowsNum, self.colsNum))
        self.checkGrid = np.zeros((self.rowsNum + self.maxShipLength, self.colsNum + self.maxShipLength))
        self.checkGrid[:self.rowsNum,:self.colsNum] = 1

    def drawBoard(self):
        plt.matshow(self.dataGrid, interpolation='nearest')
        ax = plt.gca()
        ax.set_xticks(np.arange(-.5, self.colsNum, 1));
        ax.set_yticks(np.arange(-.5, self.rowsNum, 1));
        ax.set_xticklabels(np.arange(0, self.colsNum + 1, 1))
        ax.set_yticklabels(np.arange(0, self.rowsNum + 1, 1))
        plt.grid()
        plt.show(block=False)

    def resetBoard(self):
        self.dataGrid = np.zeros((0, 0))
        self.checkGrid = np.zeros((0, 0))
        self.initDataGrid()
        plt.clf()

    def updateCell(self, x, y, value):
        self.dataGrid[int(x)][int(y)] = value
        self.drawBoard()
