#-*-coding: utf-8-*-
def Str(n):
	count=0
	for i in range(0,len(n)):
		if n[i]=='а':
			count+=1
	print(n.replace("а","о"),count,len(n))
Str(str(input()))
