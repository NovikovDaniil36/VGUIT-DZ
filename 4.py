seconds = int(input("Введите секунды:"))
minuts = 0
hours = 0 
days = 0 
if seconds >=60:
	while seconds>=60:
		seconds-=60
		minuts +=1 
if minuts >= 60:
	while minuts>= 60:
		minuts -=60
		hours +=1
if hours >=24:
	while hours>=24:
		hours-=24
		days +=1
print(days,':', hours,':', minuts,':',seconds)

