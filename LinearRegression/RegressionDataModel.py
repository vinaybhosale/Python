import collections


class LinearRegressionDataModel:

    print("Inside LinearRegressionDataModel : ")
    RegressionModel = collections.namedtuple('Data', ['xTrain', 'xTest', 'yTrain', 'yTest'])
