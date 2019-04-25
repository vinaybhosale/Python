class setMethods:
    #creating a set
    set_data = input("enter the elements for set : ")
    new_set = set(set_data)
    print(new_set)

    # iterating through set
    for elements in new_set:
        print(elements)

    # adding elements through set
    new_set.add('78')
    print("Set data after adding element : " , new_set)

    # REMOVING ELEMENTS FROM SET
    new_set.discard('78')
    print("Set data after removing element : " , new_set)
    new_set.discard('4')
    print("Set data after removing element if data matches : " , new_set)

    # intersection of sets
    days = set(["Monday","Friday","Sunday"])
    holidays = set(["Sunday","Monday","Tuesday"])
    leave = days & holidays
    print("Intersection of sets : " , leave)


    # union of sets
    data_set1 = set([1,2,3,4])
    data_set2 = set([1,2,5])
    union_data_set = data_set1|data_set2
    print("Union of sets is : ",union_data_set)

    # Clearing elements of whole set
    data_set = set([1, 2, 3, 4])
    print("Set after clearing : ",data_set.clear())

    # Symmetric difference between two sets
    type_1 = set([1,2,3,4,5,6])
    type_2 = set([5,6,8,9,7,5,6])
    print("Symmetric difference between two sets : ",type_1.symmetric_difference(type_2))

    def setDifference(self):
        color_list_1 = set(["white" , "black" , "red"])
        color_list_2 = set(["red" , "green"])

        color_difference =color_list_1 - color_list_2
        print(color_difference)

setobject = setMethods
setobject.setDifference("");