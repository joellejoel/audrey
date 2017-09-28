
even = []
constant = 4000000

def fib(n):
	if( n == 1 ):
		return 1
	if( n == 2 ):
		return 2
	return fib(n - 1) + fib(n - 2)

counter = 1

while True:	
	res = fib(counter)
	if(res > constant):
		break
	
	if(res % 2 == 0):
		even.append(res)

	counter = counter + 1

print even	
sum = 0 
for x in even:
	sum = sum + x	

print sum




