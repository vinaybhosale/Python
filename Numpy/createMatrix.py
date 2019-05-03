import numpy as np


class createMatrix:

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

cm = createMatrix()
#cm.matrix_with_numpy()
#cm.create_null_vector()
# cm.reverse_an_array()
# cm.two_d_array()
# cm.checkerboard(8)
# cm.conversion_to_array()
# cm.append_values_to_array()
# cm.check_real_imaginary()