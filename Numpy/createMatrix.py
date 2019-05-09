import numpy as np


class numpyBasics:


    def matrix_with_numpy(self):
        sample_list = [(2, 3, 4), (5, 6, 7), (8, 9, 10)]
        print(sample_list)
        matrix = np.matrix(sample_list)
        print("Creation of matrix using numpy : ", matrix)

    sample_numpy = np.arange(0, 9).reshape(3, 3)
    print(sample_numpy)

    # to create a null vector
    def create_null_vector(self):
        vector = np.zeros(10)
        print(type(vector))
        vector[np.array([6])] = 4
        print(vector)

    # to reverse an array by using numpy
    def reverse_an_array(self):
        original_array = np.arange(1, 15)
        reverse_array = original_array[::-1]
        print(reverse_array)
        print(np.flip(original_array)) # flips the array from end to start position in a reverse order

    #create 2d array with 1's on the border and 0's inside it
    def two_d_array(self):
        array = np.ones(25).reshape(5, 5)
        array[1:-1, 1:-1] = 0
        print(array)
        padded_array = np.pad(array, mode='constant', pad_width=1, constant_values=5)
        print(padded_array)

    def checkerboard(self, n):
        array = np.zeros((n, n), dtype=int)
        array[1::2, ::2] = 1
        array[::2, 1::2] = 1

        print(array)

    # convert list and tuple to array
    def conversion_to_array(self):
        input_string = input("enter the elements of list separated by space: ")
        my_list = input_string.split()
        print(my_list)
        my_array = np.asarray(my_list)
        print(my_array)

        my_tuple = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        my_tuple_array = np.asarray(my_tuple)
        print(my_tuple_array)

    def append_values_to_array(self):
        original_array = [10, 20, 30]
        new_array = np.append(original_array, [40, 50, 60])
        print(new_array)

    def check_real_imaginary(self):
        original_array = [1.00000000 + 0.j, 0.70710678 + 0.70710678j]
        x = np.sqrt([original_array])
        y = np.sqrt([original_array])

        print("Original array : x", x)
        print("Original array : y", y)
        print("Real part of the array : ")
        print(x.real)
        print(y.real)

        print("Imaginary part of the array : ")
        print(x.imag)
        print(y.imag)

    # this method finds the size of array, bytes consumed by an element, total bytes consumed by all the elements
    def array_data_info(self):
        array_sample = np.array([2, 3, 4, 5, 6])
        print(array_sample)
        print("Size of an array : ", array_sample.size)
        print("length of one array element in bytes :", array_sample.itemsize)
        print("total bytes consumed by all elements :", array_sample.nbytes)

    # this function finds out common elements from two arrays
    def sort_common_elements(self):
        array_1 = np.array([1, 2, 3, 4])
        array_2 = np.array([5, 6, 4, 7])
        common_data = np.intersect1d(array_1, array_2)
        print("common elements from two arrays : ", common_data)

    # this function finds the set difference between two arrays
    def set_difference_elements(self):
        array_1 = np.array([1, 2, 3, 4])
        array_2 = np.array([5, 6, 4, 7])
        set_array = np.setdiff1d(array_1, array_2)
        # it gives unique elements of array 1 which are not present in array 2
        print("Set difference of two array :", set_array)

    # unique values that are in only one (not both) of the input arrays.
    def set_exclusive_or(self):
        array_1 = np.array([1, 2, 3, 4])
        array_2 = np.array([5, 3, 6, 7])

        set_array = np.setxor1d(array_1, array_2)
        print("unique values from two arrays (not common): ",set_array)

    #this function compares a
    def compare_array(self):
        result_array = np.array_equal(np.array([1, 2, 3]), np.array([1, 2, 3]))
        print("The arrays are equal :", result_array)


cm = numpyBasics()
# cm.matrix_with_numpy()
# cm.create_null_vector()
# cm.reverse_an_array()
# cm.two_d_array()
# cm.checkerboard(8)
# cm.conversion_to_array()
# cm.append_values_to_array()
# cm.check_real_imaginary()
# cm.array_data_info()
# cm.sort_common_elements()
# cm.set_difference_elements()
# cm.set_exclusive_or()
cm.compare_array()