#include <iostream>
#include <cstdio>
using namespace std;

double a,b;

int main()
{
    cin >>a;
    cin >>b;
    
    int c = (int) a;
    int d = (int) b;

    printf("a+b=%10.2lf\n",a+b);
    printf("a-b=%10.2lf\n",a-b);
    printf("a*b=%10.2lf\n",a*b);
    printf("a/b=%10.2lf\n",a/b);
    printf("c/d=%10d\n", c/d);
    printf("c%%d=%10d\n", c%d);
    printf("c10=%10d\n",c);
    printf("c08=%10o\n",c);
    printf("c16=%10x\n",c);

    return 0;
}