#include <stdio.h>

/**
 * sum - add two intgers
 * @num1: the value one firsr number
 * @num2: the value one the second
 * Return: sum
 */
int sum(int num1, int num2)
{
	return (num1 + num2);
}

int main()
{
	int n;

	n = sum(7, 90);
	printf("n = %d\n", n);
	return (0);
}
