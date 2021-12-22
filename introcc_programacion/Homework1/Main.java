import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        float a = sc.nextFloat();
        a = a/3614;
        System.out.printf("%.2f\n", a);
        sc.close();
    }
}