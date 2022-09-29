def min(a,b,c):
	if a<b and a<c:
		return a 
	elif b<a and b<c:
		return b 
	else:
		return c 
a1 = int(input('Введите первое число:'))
b1 = int(input('Введите второе число:'))
c1 = int(input('Введите третье число:'))
print(min(a1,b1,c1))