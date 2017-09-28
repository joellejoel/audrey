#include<stdio.h>
#include<stdlib.h>

#define sieve_length 1000000
// #define bignumber 600851475143

void sieve(int primes[])
{
	int count = 0;
	for (int i = 2; i <= sieve_length+1; i++)
	{

		primes[i-2] = i; 
	}


	for(int i = 0; i < sieve_length-1; i++)
	{
		if(primes[i] != 0)
		{
			count += 1;
			if(count==10001)
			{
				printf("%d", primes[i]);
				break;
			}

			for(int j=i+1; j < sieve_length; j++)
			{
				if((primes[j] % primes[i]) == 0)
				{
					primes[j] = 0;
				}

			}
		}
	}

}


int main()
{
	int stuff[sieve_length] = { 0 };
	sieve(stuff);

	// for (int i = 0; i < sieve_length; i++)
	// {
	// 	printf("%d ", stuff[i]);	
	// }

	// for(int i = sieve_length-1; i >= 0; i--)
	// {
	// 	if(stuff[i] != 0)
	// 	{
	// 		if((bignumber % stuff[i])==0)
	// 		{
	// 			printf("%d", stuff[i]);
	// 			break;
	// 		}
	// 	}
	// }



	return 0;
}