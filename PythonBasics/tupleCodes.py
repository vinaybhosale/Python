from copy import deepcopy
class tuplecodes:


    #adding different datatypes in tuple
    @staticmethod
    def addtuplevalues(self):
        values = int(input("enter the size of tuple : "))
        new_tuple = ()
        reference_list = []
        for ele in range(0, values):
            elements = input("Enter the words : ")
            reference_list.append(elements)

        print(reference_list)
        new_tuple = tuple(reference_list)
        print(new_tuple)

    #to find repeated items of a tuple
    @staticmethod
    def find_repeated_elements(self):
        tuple_data = ('1', 'vinay', 'vinay', 'VINAY')
        count = 0
        element = input("Enter the element to find : ")
        count = tuple_data.count(element)

        print(count)

    #to check element present in tuple or not
    @staticmethod
    def check_element_in_tuple(self):
        tuple_data = ('1', 'vinay', 'vinay', 'VINAY')
        ele_check = input("enter the element to check : ")
        for ele in tuple_data:
            if ele == ele_check and len(ele_check) > 0:
                print("Element Exists")
            else:
                print("Element not exists")

    #to convert list to tuple
    list = [1,2,3,4,5,6]
    new_tuple = tuple(list)
    print(new_tuple)

    #remove an item from tuple
    @staticmethod
    def remove_tuple_item(self):
        tuple_data = (1,2,3,4,5)
        list_data = list(tuple_data)
        print(list_data)
        element = int(input("enter the index of element to remove from tuple :"))
        del list_data[element]
        tuple_data = tuple(list_data)
        print("Tuple after removing element : ",tuple_data)

    #slicing of tuple and reverse
    @staticmethod
    def slice_replace_tuple(self):
        tuple_data = (1, 2, 3, 4, 5, 6)
        sliced_tuple_data = tuple_data[2:5]
        print(sliced_tuple_data)

        print("Reverse of a tuple : ",tuple_data[::-1])

    #copy of a tuple
    tuple_data = (1, 2, 3, 4, 5, 6)
    copy_of_tuple = deepcopy(tuple_data)
    print("Copy of tuple :",copy_of_tuple)

# tuplecodes.addtuplevalues("")
# tuplecodes.find_repeated_elements("")
# tuplecodes.check_element_in_tuple("")
# tuplecodes.remove_tuple_item("")
tuplecodes.slice_replace_tuple("")



