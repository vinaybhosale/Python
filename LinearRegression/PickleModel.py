
import pickle

class PickleFileController:

    print("Inside Pickle ")

    @staticmethod
    def dump_Trained_Model(linearDataModel):
        print("Inside create_pickle ")
        filename = input("Enter the desired file name : ")
        file_extension = '.pkl'
        pickle_model_name = filename + file_extension
        linear_regression_data_model = open(pickle_model_name, 'wb')

        pickle.dump(linearDataModel, linear_regression_data_model)
        linear_regression_data_model.close()

        # Loading pickle model to predict y data from test_data.csv
        linear_regression_data_model = open(pickle_model_name, 'rb')


# PickleFileController.dump_Trained_Model()
