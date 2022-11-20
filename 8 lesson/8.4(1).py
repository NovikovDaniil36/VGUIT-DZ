def getDivision(a,b,c,d):

	divider = a*d
	denominator = b*c

	num1 = divider
	num2 = denominator

	while num1!=num2:
		if num1 >num2:
			num1 -= num2
		else:
			num2 -= num1

	divider/=num1
	denominator/=num1

	print(divider,'/',denominator)

getDivision(int(input('Введите делитель первого числа:')),int(input('Введите знаменатель первого числа:')),int(input('Введите делитель второго числа:')),int(input('Введите знаменатель первого числа:')))


