package javaPs;

import java.io.*;
import java.util.*;

public class P_3020 {
    static int n,h;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        int[] bot = new int[h+2];
        int[] top = new int[h+2];

        for (int i = 0; i < n / 2; i++) {
            int a = Integer.parseInt(br.readLine());
            int b = h-Integer.parseInt(br.readLine())+1;

            bot[a]++;
            top[b]++;
        }

        int min = n;
        int cnt = 0;

        for (int i = 1; i <= h; i++) {
            bot[i] += bot[i - 1];
        }
        for (int i = h; i >= 1; i--) {
            top[i] += top[i + 1];
        }

        for (int i = 1; i <= h; i++) {
            int obs = (bot[h] - bot[i - 1]) + (top[1] - top[i + 1]);

            if (obs < min) {
                min = obs;
            } else if (obs == min) {
                cnt++;
            }
        }

        System.out.println(min + " " + cnt);
    }
}
