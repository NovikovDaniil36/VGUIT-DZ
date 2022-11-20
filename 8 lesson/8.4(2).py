Radius = 0

def getCircle(x,a,y,b):

	global Radius
	Radius = ((x-a)**2)+(y-b)**2
	print(Radius)

getCircle(int(input('Введите x:')),int(input('Введите первое отклонение:')),int(input('Введите y:')),int(input('Введите второе отклонение:')))

countPoints = 0

def chekPoints(a1,b1):
	global countPoints
	if (a1**2)+(b1**2)<=Radius:
		print('True')
		countPoints += 1
	else:
		print ('False')

counter = 0

while counter<3:
	chekPoints(int(input('Введите первые координаты:')),int(input('Введите вторые координаты:')))
	counter+=1
print(countPoints)
