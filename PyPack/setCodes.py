class setMethods:
    # creating a set
    # set_data = input("enter the elements for set : ")
    # new_set = set(set_data)
    new_set = set(['1' , '2' , '3' , '4'])
    print(new_set)

    indx = 0
    brk = False
    while indx < len(new_set) and not brk:
        if new_set[indx] == '1':
            new_set.discard('1')
            brk = True

    print(new_set)
    # iterating through set
    # for elements in new_set:
    #     if elements == '1':
    #         new_set.discard('1')
    #         print(elements)
    #
    # # adding elements through set
    # new_set.add('78')
    # print("Set data after adding element : " , new_set)
    #
    # # REMOVING ELEMENTS FROM SET
    # new_set.discard('78')
    # print("Set data after removing element : " , new_set)
    #
    # # check_data = '4'
    # new_set.discard('4')
    # print("Set data after removing element if data matches : " , new_set)


#     def setDifference(self):
#         color_list_1 = set(["white" , "black" , "red"])
#         color_list_2 = set(["red" , "green"])
#
#         color_difference =color_list_1 - color_list_2
#         print(color_difference)
#
# setobject = setMethods
# setobject.setDifference("");