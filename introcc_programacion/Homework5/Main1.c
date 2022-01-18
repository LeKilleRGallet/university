#include <stdio.h>

int half(double n){
    if (n<-0.000001){
        n = n/2;
        printf("%lf\n",n);
        half(n);
        }
    return 0;
}

int main(){
    double n;
    scanf("%lf",&n);
    double i;
    scanf("%lf",&i);
    double mean = (i+n)/2;
    printf("%lf\n",mean);
    half(mean);


    return 0;
}
