from array import *

class array_examples:
    data_array = array('i' , [1,2,3,4,5])
    for elements in data_array:
        print("The elements in array are : ",elements)

    # reverse an array
    reverse_arr_data = [1,2,3,4,5,2,2,1]
    reverse_array = reverse_arr_data[::-1]
    print(reverse_array)

    # finding number of occurences of an element

    @staticmethod
    def findoccurence(value):
        value = int(input("enter the number to search : "))
        reverse_arr_data = [1, 2, 3, 4, 5, 2, 2, 1]
        count = 0
        for element in reverse_arr_data:
            if element == value:
                count += 1
        return count

    # to find first occurence of an element in array
    @staticmethod
    def firstoccurence(value):
        value = int(input("enter the number to find : "))
        arr_data = [1, 2, 3, 4, 5, 2, 2, 1]
        count = 0
        for element in arr_data:
            if element == value:
                arr_data.remove(element)
                print("loop breaked")
                print("array after removing element : ", arr_data)

    print("vinay", end=" ")
        
print(array_examples.findoccurence(""))
print(array_examples.firstoccurence(""))
# reverse_arr_data = [1,2,3,4,5,2,2,1]


