package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P_2193 {
    static long[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        dp = new long[n + 1];
        System.out.println(cal(n));
    }

    static long cal(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }

        if (dp[n] > 0) {
            return dp[n];
        }

        dp[n] = cal(n - 1) + cal(n - 2);
        return dp[n];
    }
}
