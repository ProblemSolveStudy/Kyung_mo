package javaPs;

import java.io.*;
import java.util.*;

public class P_10815 {
    static int n;
    static int[] sCard;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        sCard = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            sCard[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(sCard);
        int m = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int num = Integer.parseInt(st.nextToken());
            sb.append(binarySearch(num) + " ");
        }
        System.out.println(sb);
    }

    private static int binarySearch(int num) {
        int left =0;
        int right = n-1;

        while (left <= right) {
            int mid = (left + right) / 2;
            int target = sCard[mid];

            if(num > target) left = mid+1;
            else if(num < target) right = mid-1;
            else return 1;
        }
        return 0;
    }
}
