#_*_coding: utf-8_*_
def Length_of_members(n):
	a=[]
	while n!=0:
		n=int(input())
		a.append(n)
	print(len(a))
Length_of_members(int(input()))