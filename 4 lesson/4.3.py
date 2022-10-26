#_*_coding: utf-8_*_
def Gap(a,b):
	for i in range(a,b+1):
		if i%2!=0:
			print(i)

Gap(int(input()),int(input()))

