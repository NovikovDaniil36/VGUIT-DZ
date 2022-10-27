#_*_coding: utf-8_*_
def The_greatest_degree(n):
	a=2
	for i in range(2,n+1):
		while a*2<n:
			a*=2
	print(a)
The_greatest_degree(int(input()))