#include <iostream>
#include <cmath>

long fermatiFormuoli(long a, long b);

long partA(long n) { return ((n+1)/2); };
long partB(long n) { return ((n-1)/2); };

int main()
{
    long n = 600851475143;
    long answer = 0;
    answer = fermatiFormuoli(partA(n), partB(n));
    std::cout << answer << '\n';

    return 0;
}

long fermatiFormuoli(long a, long b)
{
    long foo = a + b;
    long bar = a - b;

    std::cout << "a is " << a << '\n';
    std::cout << "b is " << b << '\n';

    std::cout << "a + b " <<  foo << std::endl;
    std::cout << "a - b " <<  bar << std::endl;
    return 0;
}
