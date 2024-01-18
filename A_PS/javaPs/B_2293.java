package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B_2293 {
    static int n,m;
    static int[] dp;
    static int[] coins;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        dp = new int[m+1];

        dp[0] = 1;

        coins = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 1; i < n + 1; i++) {
            for (int j = coins[i]; j < m + 1; j++) {
                dp[j] += dp[j-coins[i]];
            }
        }
    }
}