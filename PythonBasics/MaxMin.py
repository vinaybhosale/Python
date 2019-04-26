class MaxMinNumber:
    def sortmaxmin(list):
        max_num = list_data[0]
        min_num = list_data[0]

        for element in list_data:
            if element > max_num:
                max_num = element
            if element < min_num:
                min_num = element
        print("Maximum number : " , max_num , "Minimum number : " , min_num)

list_elements = input("enter the elements of list : ")
list_data = list(list_elements)
print(list_data)


mmn = MaxMinNumber
mmn.sortmaxmin(list_data)
