package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_스티커 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++) {
            int n = Integer.parseInt(br.readLine());

            int[][] dp = new int[2][n];
            int[][] graph = new int[2][n];

            for(int j=0; j<2; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int k=0; k< n; k++) {
                    graph[j][k] = Integer.parseInt(st.nextToken());
                }
            }

            if (n==1) {
                int maxNum = Math.max(graph[0][0], graph[1][0]);
                System.out.println(maxNum);
            } else {
                dp[0][0] = graph[0][0];
                dp[1][0] = graph[1][0];

                dp[0][1] = graph[1][0] + graph[0][1];
                dp[1][1] = graph[0][0] + graph[1][1];

                for (int j = 2; j < n; j++) {
                    dp[0][j] = Math.max(graph[0][j] + dp[1][j - 1], dp[1][j - 2] + graph[0][j]);
                    dp[1][j] = Math.max(graph[1][j] + dp[0][j - 1], dp[0][j - 2] + graph[1][j]);
                }

                int maxVal = Math.max(dp[0][n - 1], dp[1][n - 1]);
                System.out.println(maxVal);
            }
        }
    }
}
