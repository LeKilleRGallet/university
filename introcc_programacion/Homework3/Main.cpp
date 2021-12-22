#include <iostream>
#include <cstdio>
using namespace std;

//loop that prints the five multiplication table from 'a' to 'b'

int main () {
    int a,b,i;
    cin >> a >> b;
    if (a%5 != 0) {
        i = a + 5 - a%5;
    } else {
        i = a;
    }
    while (i<=b)
    {
        printf("%d\n",i);
        i = i + 5;
    }
    
}