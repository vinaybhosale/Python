import matplotlib.pyplot as plt
import numpy as np

class ScatterPlotTwo:

    x = np.random.randn(50)
    y = np.random.randn(50)
    plt.scatter(x, y, s=70, facecolors='none', edgecolors='g')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()