import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i = 1;
        int c = 0;

        while (i<=n) {
            System.out.println(i);
            if (i==n){
                break;
            }
            if (c%2 == 0) {
                i = i +4;
            } else {
                i = i -2;
            }
            ++c;
        }

        sc.close();
    }}