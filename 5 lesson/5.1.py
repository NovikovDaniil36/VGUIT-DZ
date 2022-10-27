#_*_coding: utf-8_*_
def Degree(n):
	for i in range(1,n-1):
		while i**2<n:
			print(i**2)
			break
Degree(int(input()))