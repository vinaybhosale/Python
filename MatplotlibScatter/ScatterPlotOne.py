import matplotlib.pyplot as plt
from pylab import randn

class ScatterPlotOne:
    X = randn(200)
    Y = randn(200)
    plt.scatter(X,Y, color='r')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
