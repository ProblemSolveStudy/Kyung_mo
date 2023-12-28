package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class P_1463 {
    static int[] dp;
    static int n;

    public static void main(String[] args) throws IOException {
        /**
         * 테이블의 정의
         * dp[i] = 정수가 i를 1로 만들 때의 최소값
         *
         * 점화식
         * dp[12] = ?
         * dp[i] = min(3으로 나눌 때, 2로 나눌 때, -1 할때)
         *
         * 초기값
         * dp[0] = dp[1] = 1
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        dp = new int[n + 1];
        dp[0] = dp[1] = 0;

        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i-1] + 1;
            if(i%2 ==0) dp[i] = Math.min(dp[i], dp[i/2] + 1);
            if(i%3 ==0) dp[i] = Math.min(dp[i], dp[i/3] + 1);
        }

        System.out.println(dp[n]);
    }
}
