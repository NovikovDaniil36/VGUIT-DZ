#-*-coding: utf-8-*-
def F(a,b,c):
	if a==b and a==c:
		return '3'
	elif a!=b and b!=c and a!=c:
		return '0'
	else:
		return '2'
a1=int(input('Введите первое число:'))
b1=int(input('Введите второе число:'))
c1=int(input('Введите третье число:'))
print(F(a1,b1,c1))
