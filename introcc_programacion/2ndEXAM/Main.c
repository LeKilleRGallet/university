#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    scanf("%d",&n);
    int **matrix = (int**)malloc(n*sizeof(int*));
    for(int i=0;i<n+1;i++){
        matrix[i] = (int*)malloc(i*sizeof(int));
    }
    matrix[0][0]=1;
    for(int i=1;i<n+1;i++){
        for(int j=0;j<i;j++){
            matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j];
        }
    }
    for(int i=1;i<n+1;i++){
        for(int j=0;j<i;j++){
            printf("%d\t",matrix[i][j]);
        }
        printf("\n");
    }



    return 0;
}