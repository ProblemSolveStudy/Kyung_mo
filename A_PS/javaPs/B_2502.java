package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B_2502 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int day = Integer.parseInt(s.split(" ")[0]);
        int cnt = Integer.parseInt(s.split(" ")[1]);

        int[] dp = new int[day];
        dp[day] = cnt;


    }
}
