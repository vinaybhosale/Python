class matriceAddition:

    #take user input from user for matrice size

    r = int(input("number of rows :"))
    c = int(input("number of columns :"))
    # creating matrice A
    A = []                              # define the matrix

    # enter the elements of the list
    for ele_r in range(r):
        print(ele_r)
        row = []                        #created a blank list
        for ele_c in range(c):
            row.append(int(input()))    # here values are appended to the row list
        print("A as a list : ", A.append(row))
        print("A as a list : ", A)

    #printing the matrix A
    for ele_r in range(r):
        for ele_c in range(c):
            print(A[ele_r][ele_c], end=" ")
        print()
        print("length of A :",len(A[0]))

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

    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(len(A[0]))
    for ele_r in range(r):
        for ele_c in range(len(A[0])):
            result[ele_r][ele_c] = A[ele_r][ele_c] + B[ele_r][ele_c]
    for r in result:
        print(r)










