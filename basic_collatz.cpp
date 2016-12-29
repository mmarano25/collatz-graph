#include <iostream>

void collatz( int n )
{
	std::cout << n << ' ';
	while( n != 1 )
	{
		if( (n % 2) == 0 )
			n = n / 2;
		else
			n = (n * 3) + 1;
		std::cout << n << ' ';
	}
}

int main( )
{
	int n;
	std::cout << "Enter a number: ";
	std::cin >> n;
	collatz( n );
	return 0;
}
