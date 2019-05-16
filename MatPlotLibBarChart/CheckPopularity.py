import matplotlib.pyplot as plt
from Python.MatPlotLibBarChart.BarModulePlot import *

"""
    This Class defines the bar chart methods using matplotlib
"""

class FindPopularity(BarModulePlot):

    # def __init__(self, class_a):
    #     self.x = class_a.x
    #     self.popularity = class_a.popularity


    @staticmethod
    def plotProgramPopularity():
        """
            This method draws a bar chart according to the popularity trend
        """
        data = barmoduleplot.plotData()
        datalist = list(data)
        x = datalist[0]
        Popularity = datalist[1]
        print(x)

        x_pos = [i for i, _ in enumerate(x)]

        plt.bar(x_pos, Popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')

        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
        plt.xticks(x_pos, x)
        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        # Customize the minor grid
        # plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()

    @staticmethod
    def plotHorizontalProgramPopularity():
        """
           This method draws a bar chart according to the popularity trend with bar directions on horizontal side
        """
        data = barmoduleplot.plotData()
        datalist = list(data)
        x = datalist[0]
        Popularity = datalist[1]
        x_pos = [i for i, _ in enumerate(x)]
        plt.barh(x_pos, Popularity, color='green')
        plt.xlabel("Popularity")
        plt.ylabel("Languages")
        plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
        plt.yticks(x_pos, x)
        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()


    """
               This method draws a bar chart according to the popularity trend with bar in uniform colors
    """
    @staticmethod
    def plotUniformPopularity():
        data = barmoduleplot.plotData()
        datalist = list(data)
        x = datalist[0]
        Popularity = datalist[1]
        x_pos = [i for i, _ in enumerate(x)]

        plt.bar(x_pos, Popularity, color=(0.4, 0.6, 0.8, 1.0))

        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
        plt.xticks(x_pos, x)
        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()

    @staticmethod
    def plotDiffColorPopularity():
        """
           This method draws a bar chart according to the popularity trend with bar in different colors
        """
        data = barmoduleplot.plotData()
        datalist = list(data)
        x = datalist[0]
        Popularity = datalist[1]
        x_pos = [i for i, _ in enumerate(x)]

        plt.bar(x_pos, Popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])

        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
        plt.xticks(x_pos, x)
        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()

    @staticmethod
    def plotTextLabelBar():
        """
           This method draws a bar chart according to the popularity trend with text labels on bar
        """
        data = barmoduleplot.plotData()
        datalist = list(data)
        x = datalist[0]
        Popularity = datalist[1]
        x_pos = [i for i, _ in enumerate(x)]

        fig, ax = plt.subplots()
        rects1 = ax.bar(x_pos, Popularity, color='b')
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
        plt.xticks(x_pos, x)
        # Turn on the grid
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        # Customize the minor grid
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                        '%f' % float(height),
                        ha='center', va='bottom')

        autolabel(rects1)

        plt.show()



barmoduleplot = BarModulePlot()
data = barmoduleplot.plotData()
# FindPopularity.plotProgramPopularity()
FindPopularity.plotHorizontalProgramPopularity()
# FindPopularity.plotUniformPopularity()
# FindPopularity.plotDiffColorPopularity()
# FindPopularity.plotTextLabelBar()


