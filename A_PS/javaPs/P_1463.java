package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P_1463 {
    static int[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int number = Integer.parseInt(br.readLine());
        dp = new int[number + 1];

        System.out.println(calculate(number));
    }

    static int calculate(int num) {
        if (num == 1) {
            return 0;
        }
        if (dp[num] > 0) {
            return dp[num];
        }
        dp[num] = calculate(num-1) + 1;
        if (num % 3 == 0) {
            dp[num] = Math.min(dp[num], calculate(num / 3) + 1);
        }
        if (num % 2 == 0) {
            dp[num] = Math.min(dp[num], calculate(num / 2) + 1);
        }

        return dp[num];
    }
}
