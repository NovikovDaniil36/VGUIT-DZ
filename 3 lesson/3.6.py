#-*-coding: utf-8-*-
def chess(a,b,c,d):
	if (a+b+c+d)%2==0:
		return 'Да'
	else:
		return 'Нет'
a1 = int(input('Введите положение первой клетки по оси x:'))
b1 = int(input('Введите положение первой клетки по оси y:'))
c1 = int(input('Введите положение второй клетки по оси x:'))
d1 = int(input('Введите положение второй клетки по оси y:'))
print(chess(a1,b1,c1,d1))