
class matrixMultiplication:

    # Multiplication of matrix
    @staticmethod
    def product_of_matrix():
        # matrix1 = [[1, 1, 1],
        #            [1, 1, 1],
        #            [1, 1, 1]]
        #
        # matrix2 = [[3, 3, 3],
        #            [3, 3, 3],
        #            [3, 3, 3]]
        r = int(input("number of rows :"))
        c = int(input("number of columns :"))
        # creating matrice A
        A = []  # define the matrix

        # enter the elements of the list
        for ele_r in range(r):
            print(ele_r)
            row = []  # created a blank list
            for ele_c in range(c):
                row.append(int(input()))  # here values are appended to the row list
            print("A as a list : ", A.append(row))
            print("A as a list : ", A)

        # printing the matrix A
        for ele_r in range(r):
            for ele_c in range(c):
                print(A[ele_r][ele_c], end=" ")
            print()
            print("length of A :", len(A[0]))

        # creating matrix B

        print("creating matrix B")
        r = int(input("enter the number of rows : "))
        c = int(input("enter the number of columns : "))

        B = []

        # add elements to the matrix B
        for ele_r in range(r):
            print("row num :", ele_r)
            row = []
            for ele_c in range(c):
                print("col num :", ele_c)
                row.append(int(input()))
            B.append(row)

        # print the matrix B

        for ele_r in range(r):
            for ele_c in range(c):
                print(B[ele_r][ele_c], end=" ")
            print()
        resultant_matrix = [[0 for x in range(3)] for y in range(3)]

        print(resultant_matrix)

        for i in range(len(A)):
            print("length of matrix A : ", len(A))
            for j in range(len(B[0])):
                print("length of matrix B at zero :", len(B[0]))
                for k in range(len(B)):
                    resultant_matrix[i][j] += A[i][k] * B[k][j]
        for m in resultant_matrix:
            print(m)


matrixMultiplication.product_of_matrix()