import java.util.Scanner;

public class Sketch{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[][] matrix;
        matrix = new int[(2*n)+1][];
        for(int i = 0; i < matrix.length; i++){
            if (i<(n-1)){
                matrix[i] = new int[i+1];
            } else if((i == (n-1)) || (i == n) || (i == (n+1))) {
                matrix[i] = new int[n];
            } else if (i>(n+1)){
                matrix[i] = new int[matrix[i-1].length-1];
            }
            
        }

        for (int i = 0; i<n; i++){
            for (int j = 0; j < matrix[i].length; j++){
                matrix[i][j] = sc.nextInt();
            }
        }

        for (int j = 0; j < matrix[n].length; j++){
            for (int k = 0; k<n;k++){
            try {
                matrix[n][j] += matrix[k][j];
            } catch (IndexOutOfBoundsException e) {
                continue;}}}

        for (int i = (matrix.length-1); i > n; i--){
            for (int j = 0; j < matrix[i].length; j++){
                matrix[i][j]= matrix[i-(matrix.length-1)][j];
            }
        }

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();
        }
        sc.close();

    }}