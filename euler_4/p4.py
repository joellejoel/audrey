
palin = []
products = []


for x in range(100, 1000):
	for y in range(100, 1000):
		products.append(x*y)	

#for x in range(100, 1000):
#	for 

def palindrome(num):
	if len(str(num))  % 2 == 0:
		m_len = len(str(num)) / 2
		lenx = len(str(num))
		numby = str(num)
		status = True 
		for x in range(0, m_len):
			if numby[x] != numby[lenx - 1 - x]:
				status = False
				break
		if status == True:
			palin.append(num)

for x in products:
	palindrome(x)

sum = 0
for x in palin:
	if x > sum:
		sum = x 

print sum
