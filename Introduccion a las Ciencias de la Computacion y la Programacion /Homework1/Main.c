#include <stdio.h>
int main(){
    int a1;
    int a2;
    int a3;
    int a4;
    int a5;
    int a6;
    int a7;
    int a8;
    int a9;
    scanf(" %d%d%d%d%d%d%d%d%d", &a1, &a2, &a3, &a4, &a5, &a6, &a7, &a8, &a9 );
    int Determinante = a1*a5*a9+a4*a8*a3+a7*a2*a6-a3*a5*a7-a6*a8*a1-a9*a2*a4;
    printf("%d\n",Determinante);
    return 0;
}
