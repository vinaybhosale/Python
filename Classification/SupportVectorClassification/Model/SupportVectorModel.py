import pickle
import pandas as pd


class SupportVectorModel:

    def create_save_pickle(self, testcsv, regression_model):

        # Dump the trained decision tree classifier with Pickle
        decision_tree_pkl_filename = 'E:\Python_project\Python\Classification\SupportVectorClassification\Data\SV_Classifier_Model.pkl'

        # Write and save file in pkl format
        decision_tree_model_pkl = open(decision_tree_pkl_filename, 'wb')
        pickle.dump(regression_model, decision_tree_model_pkl)

        # Close the pickle instance
        decision_tree_model_pkl.close()

        # Loading the saved decision tree model pickle
        decision_tree_model_pkl = open(decision_tree_pkl_filename, 'rb')
        pickelmodel = pickle.load(decision_tree_model_pkl)

        df = pd.read_csv(testcsv)
        X_test = df.loc[:, ['Age', 'EstimatedSalary']]

        y_pred = pickelmodel.predict(X_test)
        print("Predicated output:", y_pred)