from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import r2_score
from Python.Regression.SupportVectorRegression.Model.PickleGenerator import *
from Python.LinearRegression.DataManipulation import *

class SupportVector:

    @staticmethod
    def display_predicted_output():

        try:
               # To read main csv file and returns train data
               # E:\Python_project\Python\Regression\SupportVectorRegression\Data\Position_Salaries.csv
               dataSet = pd.read_csv('Position_Salaries.csv')
               ds = DataController.create_Train_Test_File(dataSet)
               ds = ds[0]

               # Splitting dataset into Training set and Testing set
               x_data = ds.iloc[:, 2:].values
               y_data = ds.iloc[:, 1:2].values
               x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=1 / 3, random_state=0)

               # Feature Scaling
               x_scaler = StandardScaler()
               y_scaler = StandardScaler()
               x_train = x_scaler.fit_transform(x_train)
               x_test = y_scaler.fit_transform(x_test)

               # Fitting SVR to the dataset
               regressor = SVR(kernel='rbf')
               regressor.fit(x_train, y_train)

               # Predicting test result set
               y_predict = regressor.predict(x_test)
               accuracy = r2_score(y_test, y_predict)
               print("Accuracy is :", accuracy)

               # Set path of test csv file
               test_csv_path = input("Enter test csv path:")

               # To create and save pickle file
               Pickle_Model.create_save_pickle(test_csv_path, regressor)

        except Exception as e:
               print(e)


SupportVector.display_predicted_output()