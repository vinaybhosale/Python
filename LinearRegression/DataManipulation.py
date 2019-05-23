import pandas as pd
import collections
import os
from sklearn.model_selection import train_test_split


# Data controller is the parent class
class DataController(object):

    def __init__(self, RegressionModel):
        self.RegressionModel = RegressionModel

    """
    def DataModel(self, datamodel):

        datamodel = collections.namedtuple('Data', ['xTrain', 'xTest', 'yTrain', 'yTest'])

        return datamodel
    """

    def read_split_data(self):
        """
            This method reads the .csv file and refactor the file in size by splitting the data into  two data sets named as train data and test data
        """
        print("Inside read split data")
        try:
            filePath = input("Enter the path of file : ")
            if (filePath.endswith('.csv')):
                print("Inside read split data")
                data_set = pd.read_csv(filePath)
                print("Inside read split data 2222222")
                train_data = data_set.sample(frac=0.8)  # Splitting of dataset into train data (80%)
                test_data = pd.concat([data_set, train_data]).drop_duplicates(keep=False)  # Splitting of dataset into test data (20%)

                """
                    write the refactored train and test data into new csv  file
                    E:\Python_project\Python\LinearRegression\CSV files
                """
                train_data.to_csv('train_data.csv', header=True, index=None)

                test_data.to_csv('test_data.csv', header=True, index=None)

                data_set = pd.read_csv("train_data.csv")
                print("Inside Data Manipulation : ", type(data_set))

                type1 = "Simple"
                type2 = "Decision"
                regressiontype = input("Enter the type of regression : ")
                if regressiontype == type1:
                    independent_variable = input("Mention the independent variable : ")
                    x = data_set.columns.get_loc(independent_variable)
                    dependent_variable = input("Mention the dependent variable : ")
                    y = data_set.columns.get_loc(dependent_variable)
                    x = data_set.iloc[:, :-1]
                    print("XXXXXXXX ========== ", x)
                    y = data_set.iloc[:, 1]
                    print("YYYYYYYYYYY : ", y)
                elif regressiontype == type2:
                    x1 = data_set.columns.get_loc("temp")
                    x2 = data_set.columns.get_loc("atemp")
                    x3 = data_set.columns.get_loc("hum")
                    x4 = data_set.columns.get_loc("windspeed")
                    y = data_set.columns.get_loc("cnt")
                    x = data_set.iloc[:, [x1, x2, x3, x4]]
                    print("XXXXXXXX : ", x)
                    y = data_set.iloc[:, y:(y + 1)]
                    print("YYYYYYYY : ", y)
                if data_set[dependent_variable].isnull().sum() > 0:
                    x = x.fillna(x.mean())
                    print("XXXXXXXXXX : ", x)
                if data_set[independent_variable].isnull().sum() > 0:
                    y = y.fillna(y.mean())
                testSize = int(input("enter the size of test data : "))
                RegressionModel = train_test_split(x, y, test_size=testSize, random_state=0)
                print("Regression ========== ", RegressionModel)
                print("RegressionModel :::::::::::: ", RegressionModel)
                return RegressionModel

        except:
            print("Kindly enter the file in csv format")


    @staticmethod
    def create_Train_Test_File(csv_file):
        data_train = csv_file.sample(frac=0.8)
        data_test = pd.concat([csv_file, data_train]).drop_duplicates(keep=False)
        train_test_dir = input("Provide the directory path to save file : ")
        train_file = input("enter the train file name : ")
        test_file = input("enter the test file name : ")
        train_csv_path = train_test_dir + "/" + train_file + ".csv"
        test_csv_path = train_test_dir + "/" + test_file + ".csv"

        if not os.path.exists(train_test_dir):
            os.makedirs(train_test_dir)
        if not os.path.isfile(train_csv_path):
            data_train.to_csv(train_csv_path, header=True, index=None)
        if not os.path.isfile(test_csv_path):
            data_test.to_csv(test_csv_path, header=True, index=None)

        else:
            if not os.path.isfile(train_csv_path):
                data_train.to_csv(train_csv_path, header=True, index=None)

            if not os.path.isfile(test_csv_path):
                data_test.to_csv(test_csv_path, header=True, index=None)

        df_train = pd.read_csv(train_csv_path)

        return df_train, data_test

    @staticmethod
    def get_test_train_split_data(x_val,y_val):
        from sklearn.model_selection import train_test_split
        import collections

        # Declaring namedtuple()
        train_test_data = collections.namedtuple('train_test_data', ['x_train', 'x_test', 'y_train', 'y_test'])
        value = train_test_split(x_val, y_val, test_size=0.2)
        return train_test_data(*value)




