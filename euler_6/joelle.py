




	

def main():
	n = 100
	sum = 0
	for x in range(1, n+1):
		local_sum = x * x
		sum = sum + local_sum
	print sum

	sqsum = ((n * (n+1))/2) * ((n * (n+1))/2)

	print sqsum - sum

main()