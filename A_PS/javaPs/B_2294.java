package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B_2294 {
    static int[] dp, arr;
    static int MAX = 100001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        dp = new int[k + 1];
        arr = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.fill(dp, MAX);
        dp[0] = 0;

        for (int i = 1; i < n + 1; i++) {
            for (int j = arr[i]; j < k + 1; j++) {
                dp[j] = Math.min(dp[j], dp[j-arr[i]] + 1);
            }
        }

        if(dp[k] == MAX) System.out.println(-1);
        else System.out.println(dp[k]);
    }
}