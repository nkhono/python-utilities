## MADE JUST FOR FUN ##
## nkhono / python-utilites ##

def nameChanger(name): # Vocative
	ld = name[-1]
	tname = name[:-1]

	if(name.lower() == 'ігор'):
		tname = name
		end = 'е'

	elif(ld == 'а'):
		end = 'о'

	elif(ld in ['ь', 'й', 'р']):
		end = 'ю'

	elif(ld in ['г', 'к', 'х']):
		end = 'у'

	elif ld == 'о':
		end = 'е'

	else:
		tname = name
		end = 'е'

	return tname + end