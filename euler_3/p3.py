

prime_num = []
prime_factors = []
num = 600851475143
#num = 13195

def is_prime(num):
    return all(num % i for i in xrange(2, num))

for x in range(2, 10000):
    if(is_prime(x)):
        prime_num.append(x)

# print prime_num

for x in prime_num:
	if num % x == 0:
		num = num / x
		prime_factors.append(x)



print prime_factors
		
