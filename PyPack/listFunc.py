# to check number is present in a given list
class listFunc:
    # def alllistfunc(self):
        #to find an element is present in list
        # checkList = [1,2,3,4,5]
        # print (type(checkList))
        # num = int(input("enter the number : "))
        # print(num in checkList)
        #
        # #to check length of the list
        # listlength = len(checkList)
        # print(listlength)

        #to join elements of list and convert them into a sinlge string
        # demolist = ['v','b','p']
        # myString = demolist[0] + demolist [1] + demolist[2]
        # print(myString)
        # print("".join(map(str, demolist)))


    def join_list_data(list):
        resultstring = ''
        for n in list:
            resultstring += str(n)
        return resultstring


lfobject = listFunc
# lfobject.alllistfunc("")
listdata = [1,2,3,4,5]
print(lfobject.join_list_data(listdata))
