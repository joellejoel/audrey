			for(int j=i+1; j < sieve_length; j++)
			{
				if((j%i) == 0)
				{
					primes[j]=0;
				}
			}