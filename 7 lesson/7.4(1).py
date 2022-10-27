def Massiv(x):
	n=[]
	maxx=0
	while x!=0:
		n.append(x)
		for i in range(0,len(n)):
			if n[i]>n[i-1]:
				maxx=n[i]
		x=int(input())
	print(maxx,n.index(maxx))
Massiv(int(input()))

