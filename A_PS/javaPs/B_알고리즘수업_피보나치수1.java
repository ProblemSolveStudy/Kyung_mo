package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B_알고리즘수업_피보나치수1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int dpCnt = B_알고리즘수업_피보나치수1.dynamicFibonacci(n);
        int recurCnt = B_알고리즘수업_피보나치수1.recursionFibonacci(n);

        System.out.print(recurCnt + " " + dpCnt);
    }

    static int dynamicFibonacci(int n) {
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;

        int cnt=0;
        for (int i = 2; i < n; i++) {
            cnt++;
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return cnt;
    }

    static int recursionFibonacci(int n) {
        int cnt=0;

        if (n == 1 || n == 2) {
            cnt++;
            return 1;
        }

        return recursionFibonacci(n - 1) + recursionFibonacci(n - 2);
    }
}
