
#include <stdio.h>
#include <stdlib.h>
#include <string> 

#include <sstream>



bool is_palindrome(int n)
{
	// int num = 321; char snum[5]; 
	// convert 123 to string [buf] itoa(num, snum, 10); 
	// print our string printf("%s\n", snum);

	return false;
}

bool checkdiv(int palindrome)
{
	bool divides=false;
	for(int i=999; i>99; i--)
	{
		if((palindrome % i)==0)
		{
			if(((palindrome/i)/100)<10)
			{
				divides=true;
				break;
			}
			
		}
	}
	return divides;
}

int main()
{
	//int test_cast = 9009;
	for(int i=999; i>99; i--)
	{
		int n=(i*1000)+ ((i%10)*100) + ((i%100)-(i%10)) + (i-(i%100))/100;
		if(checkdiv(n))
		{
			printf("%d\n", n);
			break;
		}
	}

	for(int i=999; i>99; i--)
	{
		int n = (i*100) + (i%100)-(i%100) + (i-(i%100))/100;
		if(checkdiv(n))
		{
			printf("%d", n);
			break;
		}
	}
	

	return 0;
}