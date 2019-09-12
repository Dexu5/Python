x = 5

def normalx():
	x = 0

normalx()

print(x)

def globalx():
	global x
	x = 100

globalx()

print(x)