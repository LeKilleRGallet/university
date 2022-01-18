import java.util.Scanner;

//padovian sequence of numbers using reclusion
public class Main1 {

    static int padovan(int n){
        if (n==0) return 1;
        if (n==1) return 1;
        if (n==2) return 1;
        return padovan(n-2)+padovan(n-3);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        n = padovan(n);

        System.out.println(n);
        sc.close();

    }}