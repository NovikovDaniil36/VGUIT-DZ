#_*_coding: utf-8_*_
def factorial(n):
	multiplication=1
	for i in range(1,n+1):
		multiplication*=i
	
	print(multiplication)
factorial(int(input()))
