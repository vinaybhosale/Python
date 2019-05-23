import pandas as pd
import matplotlib.pyplot as plot_map
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import pickle

# Regression model algorithm for decision tree
class decisionRegression:

    # Importing dataset and splitting dataset into 2 different csv files
    file_path = input("Enter the file path : ")
    dataSet = pd.read_csv(file_path)

    training_data = dataSet.sample(frac=0.8)
    testing_data = pd.concat([dataSet, training_data]).drop_duplicates(keep=False)

    """
    df_training.to_csv('../inputFiles/training_data.csv', header=True, index=None)
    df_test.to_csv('../inputFiles/test_data.csv', header=True, index=None)
    """
    training_data.to_csv('training_data.csv', header=True, index=None)
    testing_data.to_csv('testing_data.csv', header=True, index=None)

    dataSet = pd.read_csv('training_data.csv')
    x1 = dataSet.columns.get_loc("temp")
    x2 = dataSet.columns.get_loc("atemp")
    x3 = dataSet.columns.get_loc("hum")
    x4 = dataSet.columns.get_loc("windspeed")
    y = dataSet.columns.get_loc("cnt")

    x = dataSet.iloc[:, [x1, x2, x3, x4]]
    print("XXXXXXXX : ", x)
    y = dataSet.iloc[:, y:(y+1)]
    print("YYYYYYYY : ", y)

    # Checking for null values
    if y['cnt'].isnull().sum() > 0:
        print("Taking care of null values of cnt column")
        y = y.fillna(y.mean())

    if x['temp'].isnull().sum() > 0:
        print("Taking care of null values of temp column")
        x = x.fillna(x.mean())

    # Feature Scaling
    scX = StandardScaler()
    x = scX.fit_transform(x)

    # Splitting data into training and test set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Fitting training data into model
    regression = DecisionTreeRegressor()
    regression.fit(x_train, y_train)

    # Using model to predict test data
    y_pred = regression.predict(x_test)

    plot_map.scatter(x_test, y_test, color='blue')
    plot_map.plot(x_train, regression.predict(x_train), color='black')
    plot_map.xlabel("Years Of Experience ")
    plot_map.ylabel("Salary ")
    plot_map.title("Experience vs Salary (Test Data)")
    plot_map.show()
    # Calculating accuracy
    accuracy = r2_score(y_test, y_pred)
    print("Accuracy from model is : ", accuracy)


    # Dumping model into pickle

    if accuracy > 0.8:
        file_name = '../inputFiles/DecisionTreeRegression.pkl'
        pkl_file = open('../inputFiles/DecisionTreeRegression.pkl', 'wb')
        pkl_model = pickle.dump(regression, pkl_file)

        # Load model from pickle and use same to predict test values
        pkl_file = open('../inputFiles/DecisionTreeRegression.pkl', 'rb')
        pkl_model = pickle.load(pkl_file)

        dataset_testdata = pd.read_csv('../inputFiles/test_data.csv')

        x_testdata = dataSet.iloc[:, [x1, x2, x3, x4]]
        y_testdata = dataSet.iloc[:, y:(y+1)]

        y_pred = pkl_model.predict(x_testdata)

        accuracy_pkl = r2_score(y_testdata, y_pred)

        print("Accuracy by pickle model ", accuracy_pkl)


