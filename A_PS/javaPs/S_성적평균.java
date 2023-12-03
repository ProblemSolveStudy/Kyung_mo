package javaPs;

import java.io.*;
import java.util.*;
public class S_성적평균 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        double[] nums = new double[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Long.parseLong(st.nextToken());
        }

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken()) - 1;
            int end = Integer.parseInt(st.nextToken()) - 1;

            double sum = 0;
            for (int j = start; j <= end; j++) {
                sum += nums[j];
            }
            sum /= end - start + 1;
            System.out.printf("%.2f", sum);
            System.out.println();
        }
    }
}
