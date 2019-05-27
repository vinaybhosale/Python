import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# nltk.download('stopwords')


class reviewAnalyzer:

        @staticmethod
        def data_processing():
            # Loading the data set
            filepath = input("enter the file path : ")

            """
            delimiter parameter sorts the data according to tab
            quoting = 3 remove the quotes, the parameter 3 is for removing "" quotes 
            """
            dataset = pd.read_csv(filepath, delimiter='\t', quoting=3)
            size = len(dataset)
            # print("Size of dataset : ", size, " Tab separated csv file : ", dataset )

            """
            Cleaning of dataset
            lower() This method converts all the alphabets into  lower case
            split() --> This method arranges the sentence into a list of words 
            """
            reviewList = []
            for i in range(0, 1000):
                review_dataset = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
                review_dataset = review_dataset.lower()
                review_dataset = review_dataset.split()
                ps = PorterStemmer()
                review_dataset = [ps.stem(word) for word in review_dataset if not word in set(stopwords.words('english'))]
                review_dataset = ' '.join(review_dataset)
                reviewList.append(review_dataset)
            print("review list : ", reviewList)
                # return reviewList
                # reviewAnalyzer.data_Bagging(reviewList, dataset)

        # @staticmethod
        # def data_Bagging(list , dataset):
            cv = CountVectorizer(max_features=1500)
            X = cv.fit_transform(reviewList).toarray()
            Y = dataset.iloc[:, 1].values
            print("X : ", X)
            print("Y : ", Y)
            # reviewAnalyzer.data_splitting(X, Y)

        # @staticmethod
        # # def data_splitting(data_X, data_Y):
        #     print("AAAAAAAAAAAA : ",data_X)
            x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=0)

            # Feature Scaling
            x_scaler = StandardScaler()
            y_scaler = StandardScaler()
            x_train = x_scaler.fit_transform(x_train)
            x_test = y_scaler.fit_transform(x_test)

            # Fitting the train data into decision tree classifier model
            classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
            classifier.fit(x_train, y_train)

            # Predicting test result set
            y_predict = classifier.predict(x_test)
            accuracy = accuracy_score(y_test, y_predict)
            print("Accuracy is :", accuracy)


reviewAnalyzer.data_processing()
