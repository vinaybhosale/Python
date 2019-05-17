import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import pickle

# Importing dataset and splitting dataset into 2 different csv files
csvfile = input("Enter the file path : ")
dataSet = pd.read_csv(csvfile)

df_training = dataSet.sample(frac=0.8)
df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)

"""
df_training.to_csv('../inputFiles/training_data.csv', header=True, index=None)
df_test.to_csv('../inputFiles/test_data.csv', header=True, index=None)
"""
df_training.to_csv('training_data.csv', header=True, index=None)
df_test.to_csv('test_data.csv', header=True, index=None)


dataSet = pd.read_csv('training_data.csv')
x1_index = dataSet.columns.get_loc("temp")
x2_index = dataSet.columns.get_loc("atemp")
x3_index = dataSet.columns.get_loc("hum")
x4_index = dataSet.columns.get_loc("windspeed")
y_index = dataSet.columns.get_loc("cnt")

x = dataSet.iloc[:, [x1_index, x2_index, x3_index, x4_index]]
y = dataSet.iloc[:, y_index:(y_index+1)]

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

    x_testdata = dataSet.iloc[:, [x1_index, x2_index, x3_index, x4_index]]
    y_testdata = dataSet.iloc[:, y_index:(y_index+1)]

    y_pred = pkl_model.predict(x_testdata)

    accuracy_pkl = r2_score(y_testdata, y_pred)

    print("Accuracy by pickle model ", accuracy_pkl)