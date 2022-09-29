def time(min):
	min=min%60
	hours = min//60%24
	return min,hours
minutes = int(input('Введите кол-во минут:'))
minuts,hours1 = time(minutes)
print(hours1, ':' , minuts)
