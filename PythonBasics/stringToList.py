import calendar
class stringToList:

    from PythonBasics import listFunc
    lf = listFunc.listFunc()
    lf.alllistfunc()
    def convertStrtoList(self):

        sampleData = input("Enter the numbers : ")
        newListe = list(sampleData)
        print(newListe)

    # sampleList = sampleData.split(",")
    # sampleTuple = tuple(newListe)
    # #newList = list(sampleTuple)
    # print(sampleTuple)

    def sortColor(self):
        colorlist = ["Red", "Green", "White", "Black"]
        print(colorlist)
        size = len(colorlist)
        print("First color of list is : " , colorlist[0])
        print("Last color of list is : " , colorlist[size-1])
        print(len(colorlist))

    def getCalender(self):

        mm = int(input("enter the month"))
        yy  = int(input("enter the year"))
        print(mm)
        print(calendar.month(yy, mm))

obj1 = stringToList
obj1.convertStrtoList("")
obj1.sortColor("")
obj1.getCalender("")
