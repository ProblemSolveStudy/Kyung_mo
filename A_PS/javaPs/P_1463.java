package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P_1463 {
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        dp = new int[n+1];

        System.out.println(cal(n));
    }

    static int cal(int n) {
        if (n==1) return 0;
        if(dp[n] > 0) return dp[n];

        dp[n] = cal(n-1) + 1;
        if(n%3 == 0) dp[n] = Math.min(dp[n], cal(n/3) + 1);
        if(n%2 == 0) dp[n] = Math.min(dp[n], cal(n/2) + 1);

        return dp[n];
    }
}
