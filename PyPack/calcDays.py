from datetime import date

day1 = date(2018,1,1)
day2 = date(2019,8,10)

dateDiff = day2 - day1
print(dateDiff) #shows date in days and timeformat
print(dateDiff.days) # shows only days

