

/* Dennis Pham
 * 1/28/18
 */

using System;

class EulerTwo
{
    static void Main()
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
        Console.WriteLine(print);
    }
}
