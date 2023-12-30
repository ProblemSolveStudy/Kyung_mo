package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P_1756 {
    static int d, n, pos;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        d = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        arr = new int[d+1];
        arr[0] = Integer.MAX_VALUE;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < d+1; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            arr[i] = Math.min(arr[i], arr[i - 1]);
        }

        System.out.println(Arrays.toString(arr));

        st = new StringTokenizer(br.readLine());
        pos = d+1;
        for (int i = 0; i < n; i++) {
            int size = Integer.parseInt(st.nextToken());
            binarySearch(size, 0, pos-1);
        }
        System.out.println(pos);
    }

    private static void binarySearch(int num, int start, int end) {
        while(start <= end) {
            int mid = (start + end ) / 2;
            if (num <= arr[mid]) {
                start = mid + 1;
                pos = mid;
            } else {
                end = mid - 1;
            }
        }
    }
}