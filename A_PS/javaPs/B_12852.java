package javaPs;

import java.io.*;
import java.util.*;

public class B_12852 {
    static Value[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        dp = new Value[n + 1];

        dp[1] = new Value(0, "1");

        for (int i = 2; i < n + 1; i++) {
            int cnt = Integer.MAX_VALUE;
            int before = 0;

            if (i % 3 == 0) {
                cnt = dp[i/3].n;
                before = i/3;
            }
            if (i % 2 == 0) {
                if (cnt > dp[i / 2].n) {
                    cnt = dp[i / 2].n;
                    before = i/2;
                }
            }
            if (cnt > dp[i - 1].n) {
                before = i-1;
            }

            dp[i] = new Value(dp[before].n + 1, i + " " + dp[before].ans);
        }

        System.out.println(dp[n].n);
        System.out.println(dp[n].ans);
    }
}
class Value {
    int n;
    String ans;

    public Value(int n, String ans) {
        this.n = n;
        this.ans = ans;
    }
}