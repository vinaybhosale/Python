import collections

class LinearRegressionDataModel:
    """
    It's  a Model Prepared to hold all properties which is going to be used further
    """
    RegressionModel = collections.namedtuple('Data', ['xTrain', 'xTest', 'yTrain', 'yTest'])
