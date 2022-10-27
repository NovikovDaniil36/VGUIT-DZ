#_*_coding: utf-8_*_
def More_previous(n):
	a=[]
	maxk=1
	while n!=0:
		k=1
		a.append(n)
		for i in range(0,len(a)):
			if a[i]>a[i-1]:
				k+=1
				if maxk<k:
					maxk=k
			else:
				k=1
		n=int(input())
	print(maxk)

More_previous(int(input()))