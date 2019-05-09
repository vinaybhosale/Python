import pandas as pd
import numpy as np


class oneDArray:

    @staticmethod
    def dataToSeries():

        print("Inside a method to convert a specific data type to Panda Series")
        data = pd.Series([1, 2, 3, 4, 5])
        print("One dimensional array : ", data)

        data_object = np.array(['a', 'b', 'c', 'd'])
        oneDimensionalarray = pd.Series(data_object)
        print("One dimensional array with data as objects : ", oneDimensionalarray)

    @staticmethod
    def seriesToList():
        print("Inside a method to convert Panda Series to List type")
        seriesdata = pd.Series([1, 2, 3, 4, 5])
        print("Data in series format : ", seriesdata)

        listdata = seriesdata.tolist()
        print("Data in list format : ", listdata)

    @staticmethod
    def arithmeticOperations():
        print("MEhtod to perform basic arithmetic operations on two panda series")

        seriesone = pd.Series([1, 2, 3, 4, 5])
        seriestwo = pd.Series([1, 2, 3, 4, 5])

        #Addition

        seriesAddition = seriesone + seriestwo
        print("Addition of two series is :",seriesAddition)

        #Substraction

        seriesSubstraction = seriesone - seriestwo
        print("Substraction of two series is :", seriesSubstraction)

        #Multiplication

        seriesMultiplication = seriesone * seriestwo
        print("Multiplication of two series is :", seriesMultiplication)

        #Division

        seriesDivision = seriesone/seriestwo
        print("Division of two series is :", seriesDivision)

    @staticmethod
    def powerOfElements():

        elements = np.arange(0, 7)
        print(elements)
        power = np.power(elements, 2)
        print("Power of the elements is : ", power)

    @staticmethod
    def displayDataframe():

        data = {
            'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
                     'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

        dataFrame = pd.DataFrame( data , index=labels)
        print("Data frame of the given dictionary data with index labels : ", dataFrame)
        print("Information of the data frame [eg : like getting a data type of the variable]) : ", dataFrame.info())
        print("The first three elements of the data frame are : ", dataFrame.head(3))

        # To get some specific columns from the  data frame
        print("Showing only some specific columns from a dataframe :", dataFrame[['name', 'score', 'qualify']])
        print("Showing columns and rows of a specified location : ", dataFrame.iloc[[1, 3, 5, 6], [1, 3]])
        sortedDataFrame = dataFrame[dataFrame['attempts']>2]
        print("Data frame of candidates who have attempted exam for more than two attempts :", sortedDataFrame)

        # count the number of rows and columns of a dataset
        count = dataFrame.count()
        print("The number of rows and columns of a dataframe : ",count)
#oneDArray.dataToSeries()
#oneDArray.seriesToList()
#oneDArray.arithmeticOperations()
# oneDArray.powerOfElements()
oneDArray.displayDataframe()

