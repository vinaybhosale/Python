import numpy as np


class numpyExamples:
    sample_list = [1, 2, 3, 4]
    new_array = np.array(sample_list)
    print("simple way :",  new_array)

    @staticmethod
    def list_to_numpyarray(list_1):

        new_array = np.array(list_1)
        print(new_array)


list_1 = [1, 2, 3, 4]
numpyExamples.list_to_numpyarray(list_1)