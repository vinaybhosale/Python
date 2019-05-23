from Python.LinearRegression.DataManipulation import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from Python.Classification.LogisticRegression.Model.LogisticRegressionModel import *
from sklearn.preprocessing import StandardScaler

class LogisticRegression:

    @staticmethod
    def display_predicted_output(self):

          try:
                # To read main csv file and returns train data
                dataSet = pd.read_csv('Social_Network_Ads.csv')
                ds = DataController.create_Train_Test_File(dataSet)
                ds = ds[0]

                # Get an index of columns
                x1_index = ds.columns.get_loc("Age")
                x2_index = ds.columns.get_loc("EstimatedSalary")
                y_index = ds.columns.get_loc("Purchased")

                # Splitting dataset into Training set and Testing set
                x_data = ds.iloc[:, [x1_index, x2_index]]
                y_data = ds.iloc[:, [y_index]]
                x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.25, random_state=0)

                # Feature Scaling
                x_scaler = StandardScaler()
                y_scaler = StandardScaler()
                x_train = x_scaler.fit_transform(x_train)
                x_test = y_scaler.fit_transform(x_test)

                # Fitting SVR to the dataset
                classifier = LogisticRegression(random_state=0)
                classifier.fit(x_train, y_train.values.ravel())

                # Predicting test result set
                y_predict = classifier.predict(x_test)
                accuracy = accuracy_score(y_test, y_predict)
                print("Accuracy is :", accuracy)

                # Set path of test csv file
                test_csv_path = input("Enter test csv path:")

                # To create and save pickle file
                LogisticRegressionModel.create_save_pickle(self, test_csv_path, classifier)

          except Exception as e:
            print(e)


LogisticRegression.display_predicted_output()
