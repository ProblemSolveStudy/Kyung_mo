package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P_2294 {
    static int[] dp, arr;
    static int MAX = 100001;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        dp = new int[k + 1];
        arr = new int[n + 1];
//        Arrays.fill(dp, MAX);
//        dp[0] = 0;
//
//        for (int i = 1; i <= n; i++) {
//            arr[i] = Integer.parseInt(br.readLine());
//        }
//
//        for (int i = 1; i <= n; i++) {
//            for (int j = arr[i]; j <= k; j++) {
//                dp[j] = Math.min(dp[j], dp[j - arr[i]] + 1);
//            }
//        }
//
//        if(dp[k] == MAX) System.out.println(-1);
//        else System.out.println(dp[k]);

        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);
    }
}
