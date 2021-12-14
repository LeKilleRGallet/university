import java.util.Scanner;

//ask for a number, if the number is <100, ask again until the number is >100
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while (n<100) {
            n = sc.nextInt();
        }
        System.out.println(n);
        sc.close();
    
    }}