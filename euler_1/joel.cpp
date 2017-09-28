#include<stdio.h>
#include<stdlib.h>

#define length 10

void foobar();
int eatme(int stuff);

int main()
{
	int sum = 0;
	for (int i = 1; i<length; i++)
	{
		if(i % 3 == 0)
		{
			sum += i;
			continue;
		}
		else if(i % 5 == 0)
		{
			sum += i;
			continue;
		}
	}
	printf("sum: %d\n", sum);
	foobar();
	eatme(10);

	return 0;
}

int eatme(int a)
{
	printf("ha foo bar %d \n", a);
	return 19;
}

void foobar()
{
	printf("ha foo bar \n");
}

