package javaPs;

public class P_2N타일링 {
    class Solution {
        public int solution(int n) {
            int answer = 0;
            int[] dp = new int[600001];

            dp[1] = 1;
            dp[2] = 2;

            for(int i=3; i<=n; i++) {
                dp[i] = (dp[i-2] + dp[i-1]) % 1000000007;
            }

            answer = dp[n];
            return answer;
        }
    }
}
