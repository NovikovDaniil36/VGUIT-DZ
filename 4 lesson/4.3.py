#-*-coding: utf-8-*-
def Gap(a,b):
	for i in range(a,b+1):
		if i%2!=0:
			print(i)

Gap(int(input()),int(input()))

