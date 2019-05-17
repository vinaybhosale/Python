import seaborn as sb
from matplotlib import pyplot as plt

class SeaBornCharts:


    @staticmethod
    def barPlot():
        dataset = sb.load_dataset('titanic')
        sb.barplot(x="sex", y="survived", hue="class", data=dataset)
        plt.show()

    @staticmethod
    def pointPlot():
        dataset = sb.load_dataset('titanic')
        sb.pointplot(x="sex", y="survived", hue="class", data=dataset)
        plt.show()

    @staticmethod
    def scatterPlot():
        dataset = sb.load_dataset('tips')
        sb.scatterplot(x="day", y="total_bill",  data=dataset)
        plt.show()

    @staticmethod
    def violinPlot():
        dataset = sb.load_dataset('tips')
        sb.violinplot(x="sex", y="total_bill", data=dataset)
        plt.show()


# SeaBornCharts.barPlot()
# SeaBornCharts.pointPlot()
# SeaBornCharts.scatterPlot()
SeaBornCharts.violinPlot()