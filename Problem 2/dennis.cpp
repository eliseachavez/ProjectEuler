/* Dennis Pham
 * 1/23/18
 */

#include <iostream>
using namespace std;

int main()
{
    int num1 = 0, num2 = 1, temp = 0, print = 0;
    
    while(temp < 4000001)
    {
        temp = num1 + num2;
        num1 = num2;
        num2 = temp;
        if(num2 % 2 == 0)
            print += num2;
    }
    
    cout << print << endl;
    return 0;
}
