package javaPs;

import java.util.Scanner;

public class B_2438 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 2 * (n-i) + 1; k++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
}
