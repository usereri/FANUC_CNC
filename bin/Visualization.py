import numpy as np
import matplotlib.pyplot as plt

class Visualization:

    def __init__(self) -> None:
        plt.ion()
        self.ax = plt.figure().add_subplot(projection='3d')
        self.plot_points = [[],[],[]]
        self.ax.plot(self.plot_points[0], self.plot_points[1], self.plot_points[2])
        plt.show()

    def addPoint(self, X,Y,Z):
        self.plot_points[0].append(X)
        self.plot_points[1].append(Y)
        self.plot_points[2].append(Z)
        #self.ax.plot(self.plot_points[0], self.plot_points[1], self.plot_points[2])
        #plt.draw()
        #plt.pause(0.1)

    def draw(self):
        self.ax.plot(self.plot_points[0], self.plot_points[1], self.plot_points[2])
        plt.draw()
        plt.pause(0.001)
        self.ax.cla()
        #plt.pause(999)
