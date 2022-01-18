#include <stdio.h>


int main(){
    double n;
    scanf("%lf",&n);
    double i;
    scanf("%lf",&i);
    double mean = (i+n)/2;
    printf("%.6lf\n",mean);
    while(mean<-0.000001){
        mean = mean/2;
        printf("%.6lf\n",mean);
    }

    return 0;
}
