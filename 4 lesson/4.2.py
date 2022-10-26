#_*_coding: utf-8_*_
def Gap(a,b):
	if a<b:
		for i in range(a,b+1):
			print(i)
	else:
		for i in range(a,b-1,-1):
			print(i)
Gap(int(input()),int(input()))

