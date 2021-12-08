#include <stdio.h>

//loop that sum the pairs of numbers from 1 to n

int main() {
    int n;
    scanf("%d", &n);
    int i = 2;
    while (i<=n) {
        printf("%d\n", i);
        i=i+2;
    }
    return 0;
    }