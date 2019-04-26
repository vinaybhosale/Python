import operator


class dict_examples:
    dict_data = {'value_1' : 1 , 'value_3' : 4 , 'value_2' : 2 }
    print(dict_data['value_1'])
    print("Sorted Dictionary: ", sorted(dict_data.items(), key=operator.itemgetter(1), reverse=True))

    ascending_data = list(dict_data.values())
    print("Ascending order : ", sorted(ascending_data))
    print("Descending order : ", sorted(ascending_data, reverse=True))

    #adding new key to dictionary
    sample_dict = {0:10,1:20}
    sample_dict[3] = 30
    print(sample_dict)

    # addition of two or more dictionaries
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}

    def Merge(self, dic1, dic2, dic3):
        dic3.update(dic1)
        return (dic3.update(dic2))

    print(Merge(dic1, dic2, dic3))
    print(dic3)

    #iterating over dictionary using for loop
    dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    for elements in dic1:
        print(elements)

    #print dictionary as number and its square root
    value = int(input("Enter the number : "))
    dict_data = dict()

    for elements in range(1, value):
        dict_data[elements] = elements * elements
    print(dict_data)


