#-*-coding: utf-8-*-
age = int(input('Введите свой возраст'))
name = input('Введите свое имя:')
if (age>0) and (age<75):
    if name != 'Иван':
    	if age>=16:
    		print('Поздравляем вы поступили в ВГУИТ')
    	else:
    		print('Сначала нужно окончить школу! До окончания школы вам осталось',16-age, 'лет!')
    else:
        print('Введите другое имя!')

else:
	print('Введите другой возраст')