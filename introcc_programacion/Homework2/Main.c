#include <stdio.h>

int main(){
    double x_1, y_1, x_2, y_2, b, m;
    scanf("%lf %lf %lf %lf", &x_1, &y_1, &x_2, &y_2 );

    if (x_1 == x_2 && y_1 == y_2){
        printf("Punto (%.2lf,%.2lf)\n",x_1,y_1);
    } else if (x_1 == x_2 && y_1 != y_2){
        printf("Linea Vertical x=%.2lf\n",x_1);
    } else if (x_1 != x_2 && y_1 == y_2){
        printf("Linea Horizontal y=%.2lf\n",y_1);
    } else if (x_1 != x_2 && y_1 != y_2) {
        /* y=mx+b, m=(y_2-y_1)/(x_2-x_1), b=y-mx */
        m = ((y_2-y_1)/(x_2-x_1));
        b = (y_1-m*x_1);
        if (m > 0){
            printf("Recta Creciente y=%.2lfx+%.2lf\n", m, b);
        } else if (m < 0){
            printf("Recta Decreciente y=%.2lfx+%.2lf\n", m, b);
        }
    }
return 0;
}