class scalarmultiplication:
    scalar = 3
    # Now taking matrix from user
    r = int(input("enter the number of rows :"))         #  r stands for row
    c = int(input("enter the number of columns :"))      #  c stands for column

    A = []
    B = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    for ele_r in range(r):
        ROW = []
        for ele_c in range(c):
            ROW.append(int(input()))
        A.append(ROW)
        print(range(len(A)))

    #print the matrice
    for ele_r in range(len(A)):

        for ele_c in range(len(A[0])):
            print(len(A[0]))
            B[ele_r][ele_c] = A[ele_r][ele_c] * scalar
        print("Scalar Multiplied matrice : ",B)


        print()





