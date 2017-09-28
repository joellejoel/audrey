import math

for x in range(1,334):
	for y in range(x+1, int(500-math.floor(x/2)+1)):
		z=1000-x-y
		if ((x*x) + (y*y) == (z*z)):
			print x*y*z
			break

# print(math.floor(123.123))