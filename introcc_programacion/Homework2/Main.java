import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double x_1 = sc.nextDouble();
        double y_1 = sc.nextDouble();
        double r_1 = sc.nextDouble();
        double x_2 = sc.nextDouble();
        double y_2 = sc.nextDouble();
        
        double d = Math.pow(Math.pow(x_2-x_1, 2)+Math.pow(y_2-y_1, 2), 0.5);
        
        if (d <= r_1){
            System.out.println("yes"); 
        } else {
            System.out.println("no");
        }
        sc.close();
    }}