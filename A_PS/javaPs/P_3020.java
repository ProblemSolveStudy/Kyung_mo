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

        int[] down = new int[h+2];
        int[] up = new int[h+2];

        for (int i = 0; i < n / 2; i++) {
            int a = Integer.parseInt(br.readLine());
            int b = h-Integer.parseInt(br.readLine())+1;

            down[a]++;
            up[b]++;
        }

        Arrays.sort(down);
        Arrays.sort(up);

        for (int i = 1; i <= h; i++) {
            down[i] += down[i-1];
        }
        for (int i = h; i >= 1; i--) {
            up[i] += up[i + 1];
        }
    }
}
