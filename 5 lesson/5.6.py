#_*_coding: utf-8_*_
def Average_value(n):
	a=[]
	summ=0
	while n!=0:
		summ+=n
		n=int(input())
		a.append(n)
	print(summ/len(a))
Average_value(int(input()))