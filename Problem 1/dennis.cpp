/* Dennis Pham
 * 1/19/18
 */

#include <iostream>

using namespace std;

int main()
{
    int three = 0, five = 0;
    int x = 0, y= 0;
    
    for(int i = 1; x < 1000; i++)
    {
        x = i * 3;
        y = i * 5;
        
        if(x < 1000)
            three += x;
        
        if(y < 1000)
            five += y;
        
        //subtract x if the value is calculated as a multiple of five.
        if(x % 5 == 0)
            three -= x;
    }
    
    cout << "total " << three + five << endl;
    return 0;
}
