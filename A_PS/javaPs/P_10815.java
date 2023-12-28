package javaPs;

import java.io.*;
import java.util.*;

public class P_10815 {
    static int n;
    static int[] sCard;

    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        sCard = new int[n];
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
        int start = 0;
        int end = n-1;

        while(start<=end) {
            int mid = (start+end) / 2;
            int target = sCard[mid];

            if(num > target) start = mid + 1;
            else if (num < target) end = mid - 1;
            else return 1;
        }
        return 0;
    }
}
