
constant = 400000


x = 1
y = 2
sum = 2
while True:	
	total = x + y
	if( total > constant):
		break

	if( total % 2 == 0 ):
		sum = sum + total

	x = y
	y = total


print sum




