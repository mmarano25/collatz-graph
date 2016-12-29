#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>


// utility functions 
	template< typename T >
void print_vector( std::vector<T> v )
{
	std::copy( std::begin( v ), std::end( v ),
			std::ostream_iterator<T>( std::cout, " " ) );
}

int collatz_step( int n )
{ //executes one step of the collatz conject
	if( (n % 2 ) == 0 )
		return ( n / 2 );
	else
		return ( ( n * 3 ) + 1 );
}



// main functions 
std::vector<int> store_collatz( int n )
{
	std::vector<int> result;
	result.push_back( n );
	while( n != 1 )
	{
		n = collatz_step( n );
		result.push_back( n );
	}
	return result;
}


int main( )
{
	int n;
	std::cout << "Enter a number: ";
	std::cin >> n;
	std::vector<int> stored_collatz = store_collatz( n );

	print_vector<int>( stored_collatz );
	std::cout << std::endl;
	return 0;
}
