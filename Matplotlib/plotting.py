from matplotlib import pyplot as plt
import pandas as pd


class matplotlibBasics:

    # plot a simple graph
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

    # plotting a graph by taking values from an external file
    @staticmethod
    def plot_values_of_textfile():

        file = input("Enter the file name : ")
        with open(file) as f:
            data = f.read()
        data = data.split('\n')

        print("AAAAAAAAA", data)
        x = [int(row.split(' ')[0]) for row in data]
        y = [int(row.split(' ')[1]) for row in data]
        plt.plot(x, y)
        plt.xlabel("X-AXIS")
        plt.ylabel("Y-AXIS")
        plt.title("Value from .txt file")
        plt.show()

    #plotting line charts for a range (1 jan to 30 jan) from data stored in csv file
    @staticmethod
    def plot_line_chart_of_csv_file():
        # try:
            df = pd.read_csv('docdata.csv')
            print(df)
            df.plot()
            plt.show()

        # except(FileNotFoundError):
        #     print("Code Executed In Catch Block")

    # Plotting two lines in a same plot with legends
    @staticmethod
    def plot_two_lines_with_legends():
        x1 = [10, 20, 30]
        y1 = [20, 40, 10]
        # plotting the line 1 points
        plt.plot(x1, y1, label="line 1")
        # line 2 points
        x2 = [10, 20, 30]
        y2 = [40, 10, 30]
        # plotting the line 2 points
        plt.plot(x2, y2, label="line 2")
        plt.xlabel('x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('y - axis')
        # Set a title of the current axes.
        plt.title('Two or more lines on same plot with suitable legends ')
        # show a legend on the plot
        # plt.legend()
        # Display a figure.
        plt.show()
# matplotlibBasics.simpleplot()
# matplotlibBasics.plot_by_values()
# matplotlibBasics.plot_values_of_textfile()
# matplotlibBasics.plot_line_chart_of_csv_file()
matplotlibBasics.plot_two_lines_with_legends()