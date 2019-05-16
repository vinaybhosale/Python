import pandas as pd
import collections
from sklearn.model_selection import train_test_split

#Data controller is the parent class
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
                """
                train_data.to_csv('train_data_file.csv', header=True, index=None)
                test_data.to_csv('test_data_file.csv', header=True, index=None)

                data_set = pd.read_csv('train_data_file.csv')
                x = data_set.iloc[:, :-1].values
                y = data_set.iloc[:, 1].values

                if data_set['Salary'].isnull().sum() > 0:
                    x = x.fillna(x.mean())
                    print("XXXXXXXXXX : ", x)
                if data_set['YearsExperience'].isnull().sum() > 0:
                    y = y.fillna(y.mean())
                testSize = int(input("enter the size of test data : "))
                RegressionModel = train_test_split(x, y, test_size=testSize, random_state=0)

                print("RegressionModel :::::::::::: ", RegressionModel)
                return RegressionModel

        except:
            print("Kindly enter the file in csv format")



























"""

        def get_data(self):
       
        try:
            # filePath = input("Enter the path of file : ")
            # if(filePath.endswith('.csv')):
            #     data_set = pd.read_csv(filePath)
            #     x = data_set.iloc[:, :-1].values
            #     print("value stored in x : ", x)
            #     y = data_set.iloc[:, 1].values
            #     print("value stored in y : ", y)
            print("Inside get data method")
            data1, data2 = DataController.read_split_data()
            print("SSSSSSSSS:",data1)
            print("SSSSSSSSS:", data2)
            testSize = int(input("enter the size of test data : "))
            # RegressionModel = train_test_split(x, y, test_size=testSize, random_state=0)
            #
            # print("RegressionModel :::::::::::: ", RegressionModel)
            # return RegressionModel

        except:
            print("Kindly enter the file in csv format")
"""