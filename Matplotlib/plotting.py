from matplotlib import pyplot as plt


class matplotlibBasics:

    @staticmethod
    def simpleplot():
        plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
        plt.xlabel("X_AXIS")
        plt.ylabel("Y-AXIS")
        plt.title("SIMPLE PLOT")
        print(plt.show())

    @staticmethod
    def plot_by_values():
        x = [1, 5, 2]
        y = [2, 5, 1]
        plt.plot(x, y)
        plt.xlabel("X-data")
        plt.ylabel("Y-data")
        plt.title("Plot By Values")
        plt.show()

    @staticmethod
    def plot_values_of_textfile():

        file = input("Enter the file name : ")
        with open(file) as f:
            data = f.read()
        data = data.split('\n')
        x = [row.split(' ')[0] for row in data]
        y = [row.split(' ')[1] for row in data]
        plt.plot(x, y)
        plt.xlabel("X-AXIS")
        plt.ylabel("Y-AXIS")
        plt.title("Value from .txt file")
        plt.show()
# matplotlibBasics.simpleplot()
# matplotlibBasics.plot_by_values()
matplotlibBasics.plot_values_of_textfile()