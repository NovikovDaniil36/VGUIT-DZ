#-*-coding: utf-8-*-
def Massiv(x):
	n=[]
	b=[]
	while x!=0:
		n.append(x)
		x=int(input())
		for i in range(0,len(n)):
			if n[i]%2!=0:
				b.append(n[i])
				n.pop(i)
	b.sort(reverse=True)
	print(b)
Massiv(int(input()))

