#include <stdio.h>

//print all the numbers from n to 0

int main(){
    int n, i;
    scanf("%d",&n);
    for ( i = n; i >= 0; i--)
    {
        printf("%d\n",i);
    }
    
    return 0;
}