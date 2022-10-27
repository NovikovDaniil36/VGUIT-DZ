#-*-coding: utf-8-*-
def Gap(a,b):
	if a<b:
		for i in range(a,b+1):
			print(i)
	else:
		for i in range(a,b-1,-1):
			print(i)
Gap(int(input()),int(input()))

