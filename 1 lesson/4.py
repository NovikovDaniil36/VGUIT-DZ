seconds = int(input("Введите секунды:"))
days = seconds//3600//24
seconds -= days*3600*24
hours = seconds//3600 
seconds -= hours*3600
minutes = seconds // 60
seconds -= minutes * 60
print(days, ':', hours,':',minutes,':',seconds)


