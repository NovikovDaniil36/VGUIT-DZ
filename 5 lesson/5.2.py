#_*_coding: utf-8_*_
def Natural_divisor(n):
	if n>2:
		for i in range(2,n+1):
			if n%i==0:
				print(i)
Natural_divisor(int(input()))