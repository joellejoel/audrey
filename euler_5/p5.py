

num = 2520

while (1):
	#print x
	truth = True
	for x in range(2, 20):
		if (num % x != 0):
			truth = False
			break

	if truth == True:
		print num
		break
	else:
		num = num + 1

