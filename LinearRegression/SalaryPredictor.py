#Simple Liner Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot


class SalaryPredictor:

    #Load the dataset
    dataset = pd.read_csv("Salary_Data.csv")
    print(dataset.head())
    x_data = dataset.iloc[:, :-1].values
    y_data = dataset.iloc[:, 1].values

    #Splitting the data in training data and testing data
    from sklearn.model_selection import train_test_split
    # RegressionModel = train_test_split(x, y, test_size=10, random_state=0)
    x_data_train, x_data_test, y_data_train, y_data_test = train_test_split(x_data, y_data, test_size=10, random_state=0)

    #simple linear regression
    from sklearn.linear_model import LinearRegression
    linearModel = LinearRegression()
    linearModel.fit(x_data_train, y_data_train)
    predicted_data = linearModel.predict(x_data_test)
    print("Predicted data is : ", predicted_data)

    #plot the training data on a scatter
    plot.scatter(x_data_train, y_data_train, color='red')
    plot.plot(x_data_train, linearModel.predict(x_data_train), color='black')
    plot.xlabel("Years Of Experience")
    plot.ylabel("Salary")
    plot.title("Experience vs Salary (Train Data)")
    plot.show()

    #plot the test data on a scatter plot
    plot.scatter(x_data_test, y_data_test, color='blue')
    plot.plot(x_data_train, linearModel.predict(x_data_train), color='black')
    plot.xlabel("Years Of Experience ")
    plot.ylabel("Salary ")
    plot.title("Experience vs Salary (Test Data)")
    plot.show()
