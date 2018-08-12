//STATUS: SOLVED

#include <iostream>
//using namespace std;


int main()
{
	int i = 0;
	int sum = 0;
	for (i = 0; i < 1000; i++)
		if (i%3 == 0 | i%5==0)
		sum = i + sum;
	std::cout << "The sum of all multiples of 3 and 5 under 1000 is: " << sum << std::endl;

return 0;
}
