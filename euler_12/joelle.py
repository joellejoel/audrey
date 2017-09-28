
for x in range(1, 10000):
	holder = ((x*(x+1))/2)
	arr = []

	for y in range(1,holder+1):
		if (holder % y == 0):
			# print holder
			arr.append(y)
	if ((len(arr)) > 5):
		print str(holder)	
		print arr
		break
	# print arr
	#print str(holder) + " has " + str(len(arr)) + " divisors " 