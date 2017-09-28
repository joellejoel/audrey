
all_num = range(2,12000)
prime_arr = []

global_sum = 0
global_counter = 0 

def is_prime(num):
    return all(num % i for i in xrange(2, num))

for x in range(0, len(all_num)):
    if(is_prime(x)):
        prime_arr.append(x)

print "here"

for x in range(0, len(prime_arr)):
	#print "----------------------"
	for y in range(x, len(prime_arr)):
		sum = 0
		counter = 0
		for z in range(x, y+1):
			sum = sum + prime_arr[z]
			counter = counter + 1
		if(is_prime(sum)):
			if(sum < 1000000):
				if(counter > global_counter):
					global_sum = sum
					global_counter = counter
			else:
				break

print global_sum
print global_counter

		#print "----------------------"
		#for z in range(0, x):
		#	print " ",
		#for z in range(x, y+1):
		#	print z,
		#print ""
		#print x,y	
		
