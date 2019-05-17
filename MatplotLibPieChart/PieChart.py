import matplotlib.pyplot as plt
from Python.MatplotLibPieChart.PieData import *

class PieChart:

    @staticmethod
    def popularityByPie():
        # Data to plot
        data = pie_data.plotData()
        datalist = list(data)
        x = datalist[0]
        Popularity = datalist[1]
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
        # explode 1st slice
        explode = (0.1, 0, 0, 0, 0, 0)
        # Plot
        plt.pie(Popularity, explode=explode, labels=x, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')

        """
            This line of code adds a title to pie chart
        """
        plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago",
                  bbox={'facecolor': '0.8', 'pad': 5})
        plt.show()

PieChart.popularityByPie()



