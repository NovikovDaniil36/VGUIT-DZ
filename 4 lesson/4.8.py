#_*_coding: utf-8_*_
def ladder(n):
	a=[]
	if n<=9:
		for i in range(1,n+1):
			a.append(i)
			print(a)
	else:
		print('Введите число меньше 10!')

ladder(int(input()))
