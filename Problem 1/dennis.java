class EulerOne
{
    public static void main(String[] args)
    {
        int foo = 0;
        int bar = 0;
        int x = 0;
        int y = 0;

        for(int i = 1; x < 1000; i++)
        {
            x = i * 3;
            y = i * 5;
            if(x < 1000)
                foo += x;
            if(y < 1000)
                bar += y;
            if(x % 5 == 0)
                foo -= x;
        }
        System.out.println(foo + bar);
    }
}
