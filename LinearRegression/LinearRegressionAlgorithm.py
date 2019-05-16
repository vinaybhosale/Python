from Python.LinearRegression.DataManipulation import *
from Python.LinearRegression.RegressionDataModel import *
from sklearn.linear_model import LinearRegression
from Python.LinearRegression.PickleModel import *
from sklearn.metrics import r2_score
import matplotlib.pyplot as plot
import pickle

"""  DataTrainer is Child class Derived from DataController Class   """
class DataTrainer(DataController):

    def __init__(self):

        # Passing Model To Parent Class
        DataController.__init__(self, LinearRegressionDataModel.RegressionModel)

    def trainUserData(self):

        linearDataModel = LinearRegression()
        dataset = DataController.read_split_data(self)
        print("Data Set : ", dataset)
        dataset = LinearRegressionDataModel.RegressionModel(*dataset)
        print("LinearRegressionDataModel RegressionModel : ", dataset)
        linearDataModel.fit(dataset.xTrain, dataset.yTrain)

        predicted_data = linearDataModel.predict(dataset.xTest)
        print("Predicted data is : ", predicted_data)

        """
            Now Calculate the accuracy of the model
        """
        dataAccuracy = r2_score(dataset.yTest, predicted_data)
        print("Accuracy of the model is : ", dataAccuracy)

        filename = input("Enter the desired file name : ")
        file_extension = '.pkl'
        pickle_model_name = filename + file_extension
        linear_regression_data_model = open(pickle_model_name, 'wb')
        pickle.dump(linearDataModel, linear_regression_data_model)
        linear_regression_data_model.close()

        # Loading pickle model to predict y data from test_data.csv
        linear_regression_data_model = open(pickle_model_name, 'rb')


        """
             calling methods for drawing Graph       
             param:regression model,dependant and independant Variable
             """
        # plotting train Data
        DataTrainer.PlotGraph(self, linearDataModel, dataset.xTrain, dataset.yTrain)
        # Plotting Test Data
        DataTrainer.PlotGraph(self, linearDataModel, dataset.xTest, dataset.yTest)


    # Method to draw a graph
    def PlotGraph(self, linearDataModel, x_data, y_data):
        plot.scatter(x_data, y_data, color='Red')
        plot.plot(x_data, linearDataModel.predict(x_data), color='blue')
        plot.title("Salary Vs Experience")
        plot.xlabel("Years Of Experience")
        plot.ylabel("Salary")
        plot.show()


datatrainer = DataTrainer()
datatrainer.trainUserData()