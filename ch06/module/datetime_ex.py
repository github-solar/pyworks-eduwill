import datetime

now = datetime.datetime.now()
#today = datetime.datetime.today()
print(now)
#print(today)

print("{}년".format(now.year))
print("{}월".format(now.month))
print("{}일".format(now.day))
print("{}시".format(now.hour))
print("{}분".format(now.minute))
print("{}초".format(now.second))

print(now.strftime("%Y년 %m월 %d일 %H:%M:%D"))

