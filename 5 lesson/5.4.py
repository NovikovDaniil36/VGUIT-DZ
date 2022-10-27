#_*_coding: utf-8_*_
def Sportsman(x,y):
	tan_procent=(10*x)/100
	days=0
	while x<y:
		x+=tan_procent
		days+=1
	print(days)
Sportsman(int(input()),int(input()))