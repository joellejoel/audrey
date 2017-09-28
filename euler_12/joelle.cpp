#include<stdio.h>
#include<stdlib.h>

#define sieve_length 500000
#define n 100000

void sieve(int primes[])
{

	for (int i = 2; i <= sieve_length+1; i++)
	{

		primes[i-2] = i; 
	}


	for(int i = 0; i < sieve_length-1; i++)
	{
		if(primes[i] != 0)
		{


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


void prime_factors(int power_arr[], int m, int sieve_arr[])
{
	if(m%2==0)
	{
		m = m/2;
		for(int i=0; i<m; i++)
		{
			if(sieve_arr[i]!= 0)
			{
				int num = m;
				while(num % sieve_arr[i] == 0)
				{
					num = num/sieve_arr[i];
					power_arr[i] += 1;
				}
			}
		}
	}

	else 
	{
		for(int i=0; i<m; i++)
		{
			if(sieve_arr[i]!= 0)
			{
				int num = m;
				while(num % sieve_arr[i] == 0)
				{
					num = num/sieve_arr[i];
					power_arr[i] += 1;
				}
			}
		}
	}
}


int main()
{
	int stuff[sieve_length] = { 0 };
	sieve(stuff);

	for(int i = 0; i<3; i++)
	{
		printf("%d\n", stuff[i]);
	}
			printf("||||||||||||\n");


	int local_a[sieve_length]={0};
	prime_factors(local_a, 1, stuff);
	
	
	for(int i = 1; i < n ; i++)
	{
		// local_a = primefactors_of_n() // should return arr
		// local_b = primefactors_of_nplusone() // should return arr
		printf("i is %d\n", i);
		
		int local_b[sieve_length]={0};

		prime_factors(local_b, i+1, stuff);

		// printf("local_a is \n");
		// for(int i = 0; i<5; i++)
		// {
		// 	printf("%d\n", local_a[i]);
		// }
		
		// printf("local_b is \n");
		// for(int i = 0; i<5; i++)
		// {
		// 	printf("%d\n", local_b[i]);
		// }

		int num_div = 1;

		for (int k=0; k<sieve_length; k++)
		{

			// iterate both arr at the same time
			if (local_a[k] != 0 || local_b[k] != 0)
			{
				num_div = num_div * (local_a[k]+local_b[k] +1);
				//printf("num_div is %d\n", num_div);
			} 

		}
		if(num_div>500)
		{
			printf("%d\n", i);
			break;
		}

		for(int i=0; i<sieve_length; i++)
		{
			local_a[i] = local_b[i];
		}


	}
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