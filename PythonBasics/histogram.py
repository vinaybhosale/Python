class histogram:
    def createhistogram(listdata):

        for data in listdata:
            output =''
            dataoccurence = data
            while(dataoccurence > 0):
                output += '!'
                dataoccurence = dataoccurence - 1
                print(output)
listdata = [1,2,3,4]
hist = histogram
hist.createhistogram(listdata)