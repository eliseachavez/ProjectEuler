/* Dennis Pham
 * 1/23/17
 */

#include <iostream>
using namespace std;

int main()
{
    long num1 = 0, num2 = 1, print = 0;
    long temp = 0;
    for(int i = 0; temp < 4000001; i++)
    {
        temp = num1 + num2;
        num1 = num2;
        num2 = temp;
        if(num2 % 2 == 0)
            print += num2;
        cout << "first number " << num1 << " second number " << num2 << endl;
    }
    
    cout << print << endl;
    return 0;
}
