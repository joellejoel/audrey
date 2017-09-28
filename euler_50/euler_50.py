
all_num = range(2,20000) 
prime_num = []
#print len(all_num)


def is_prime(num):
	return all(num % i for i in xrange(2, num))

for x in range(0, len(all_num)):
	if(is_prime(x)):
		prime_num.append(x)

global_sum = 0
global_counter = 0

for x in range(0, len(prime_num)):
	# x prints index	
	for y in range(x, len(prime_num)):

# generate a list of prime number below 800k 

# check if outcome is a prime

# check if outcome is larger than 1 million 

# if outcome is a prime, do next else end

# if outcome is larger than 1 million, end print all

# if outcome is smaller replace variable MAX and add COUNTER + 1



