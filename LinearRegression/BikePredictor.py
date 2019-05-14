#linear Regression algorithm to predict Bike Users vs Temparature


import pandas as pd
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split


class BikePredictor:

    try:
        #Loading the data from csv file
        userdata = pd.read_csv("bike_sharing.csv")
        print(userdata.head(10))

        #Renamed the column names
        userdata.rename(columns={"temp": "Temperature", "cnt": "Shared Bikes"}, inplace=True)
        print(userdata)
        columns = userdata.columns
        print(columns)
        x_data = userdata.loc[:, ['Temperature']].values
        y_data = userdata.loc[:, ['Shared Bikes']].values

        #Splitting the data set into training data and testign data
        x_train_data, x_test, y_train_data, y_test = train_test_split(x_data, y_data, test_size=8500, random_state=True)

        #Using Linear regression module to predict the outcome
        from sklearn.linear_model import LinearRegression
        linear_module = LinearRegression()
        linear_module.fit(x_train_data, y_train_data)
        predictions = linear_module.predict(x_test)
        print(predictions)

        #graph for training data
        plot.scatter(x_train_data, y_train_data, color = 'red')
        plot.plot(x_train_data, linear_module.predict(x_train_data), color='black')
        plot.xlabel("Temperature")
        plot.ylabel("Shared Bikes")
        plot.title("Shared Bikes vs Temperature")
        plot.show()

        #graph for testing data
        plot.scatter(x_test, y_test, color='yellow')
        plot.plot(x_train_data, linear_module.predict(x_train_data))
        plot.xlabel("Temperature")
        plot.ylabel("Shared Bikes")
        plot.title("Shared Bikes vs Temperature")
        plot.show()

    except FileNotFoundError:
        print("File not found")








