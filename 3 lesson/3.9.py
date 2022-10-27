#-*-coding: utf-8-*-
def chocolate(n,m,k):
	if k<n*m and ((k%n==0) or (k%m==0)):
		return 'Да'
	else:
		return 'Нет'
n1=int(input('Введите длину шоколадки:'))
m1=int(input('Введите ширину шоколадки:'))
k1=int(input('Введите кол-во долек:'))
print(chocolate(n1,m1,k1))