#-*-coding: utf-8-*-
def yers(a):
	if (a%4==0 or a%400==0) and a%100!=0:
		return 'Да'
	else:
		return 'Нет'
a1=int(input('Введите год:'))
print(yers(a1))