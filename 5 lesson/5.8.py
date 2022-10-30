#-*-coding: utf-8-*-
def More_in_a_row(n):
	a=[]
	max_quantity=0
	while n!=0:
		quantity=0
		a.append(n)
		for i in range(0,len(a)):
			if a[i]==a[i-1]:
				quantity+=1
				if max_quantity<quantity:
					max_quantity=quantity
			else:
				quantity=1
		n=int(input())
	print(max_quantity)

More_in_a_row(int(input()))