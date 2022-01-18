import java.util.Scanner;

public class Main2 {

    static int padovan(int n){
        int padovan = 0;
        int padovan_prev = 0;
        int padovan_secprev = 0;
        int padovan_thirprev = 0;
        for (int i = 0; i <= n; i++) {
            if (i == 0) {
                padovan = 1;
            } else if (i == 1) {
                padovan = 1;
            } else if (i == 2) {
                padovan = 1;
            } else {
                padovan = padovan_secprev+padovan_thirprev;
            }
            padovan_thirprev = padovan_secprev;
            padovan_secprev = padovan_prev;
            padovan_prev = padovan;
            
        }
        return padovan;
        }
        
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        n = padovan(n);

        System.out.println(n);
        sc.close();

    }}