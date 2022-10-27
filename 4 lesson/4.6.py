#-*-coding: utf-8-*-
def factorial(n):
	multiplication=1
	for i in range(1,n+1):
		multiplication*=i
	
	print(multiplication)
factorial(int(input()))

