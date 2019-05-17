
class Pie_Data(object):

    def __init__(self):
        self.x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        self.popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]


    def plotData(self):
        self.list_x = self.x
        self.list_popularity = self.popularity

        return self.list_x, self.list_popularity


pie_data = Pie_Data()
pie_data.plotData()

