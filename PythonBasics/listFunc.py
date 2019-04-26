# to check number is present in a given list
import operator


class listFunc:
    # def alllistfunc(self):
        #to find an element is present in list
        # checkList = [1,2,3,4,5]
        # print (type(checkList))
        # num = int(input("enter the number : "))
        # print(num in checkList)

        #to check length of the list
        # listlength = len(checkList)
        # print(listlength)

        #to join elements of list and convert them into a sinlge string
        # demolist = ['v','b','p']
        # myString = demolist[0] + demolist [1] + demolist[2]
        # print(myString)
        # print("".join(map(str, demolist)))


    # def join_list_data(list):
    #     resultstring = ''
    #     for n in list:
    #         resultstring += str(n)
    #     return resultstring

    # ADDITION OF LIST
    # list = [1,2,3,4,5]
    # print(len(list))
    # total = 0
    # listmultiply = 1
    # for element in range(0 , len(list)):
    #     print("aaaa : ",list[element] , "bbbb : ",element)
    #     total = total + list[element]
    # print(total)

    # MULTIPLICATION OF LIST
    # for element in list:
    #     listmultiply = listmultiply * element
    # print(listmultiply)

    # SMALLEST ELEMENT IN LIST
    # list_data = [2,3,4,5,6]
    # print("prints minimum value from list : ", min(list_data))
    # print("prints maximum value from list : ", max(list_data))

    # sample_list = ['abc', 'xyz', 'aba', '1221']
    # count = 0
    # for ele in sample_list:
    #     first_char = ele[0]
    #     if len(ele) >= 2 and ele.endswith(first_char):
    #         count += 1
    # print("Number of Strings with same start & end char :", count)

    #sorting of list of tuples according to the end tuple character
    # samplelist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    # var = sorted(samplelist, key=operator.itemgetter(1))
    # print("sorting of list with end char of tuple : ", var)

    #remove duplicate elements from list
    # duplicatelist = [1,2,1,3,1,5,5,4,3]
    # neset = set(duplicatelist)
    # nelist = list(neset)
    # print(sorted(nelist))
    # print(neset)

    #creating copy of a list
    # old_list = [1,2,3,4,5]
    # new_list = old_list.copy()
    # print("copy of list : ", new_list)

    #to remove string which is bigger in size
    # size_list = ["Vinay", "JonSNow", "WhiteWalker", "Valar", "Morghulis"]
    # size = int(input("enter the size : "))
    # print(len(size_list[0]))
    # for ele in size_list:
    #     if len(ele) <= size:
    #         print("asd", size_list.remove(ele))
    # print(size_list)


    def compare_list(self, list_1, list_2):
        result = False
        for ele_x in list_1:
            for ele_y in list_2:
                if ele_x == ele_y:
                    result = True
        return result



lfobject = listFunc()
print(lfobject.compare_list([1,2,3,45] , [8,9,6,45]))
# lfobject.alllistfunc()
# listdata = [1,2,3,4,5]
# print(lfobject.join_list_data(listdata))



















