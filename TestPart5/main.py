import datetime, time

bdDay = int(input("Введите день вашего рождения: "))
bdMonth = int(input("Введите месяц вашего рождения: "))
bdYear = int(input("Введите год вашего рождения: "))

dt = datetime.datetime(bdYear, bdMonth, bdDay)
ts = int(dt.timestamp())
now = int(time.time())

print(now - ts)