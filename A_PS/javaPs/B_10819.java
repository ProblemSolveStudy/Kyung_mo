package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.*;

/**
 * 순열 구한 후 순열에서 가장 최대값을 가지도록 구함
 */
public class B_10819 {
    static int n;
    static int result = Integer.MIN_VALUE;
    static int[] arr, selected;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        visited = new boolean[n];

        selected = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        backTracking(0);
        System.out.println(result);
    }

    private static void backTracking(int cnt) {
        if (cnt == n) {
            result = Math.max(result, getResult());
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                selected[cnt] = arr[i];
                backTracking(cnt + 1);
                visited[i] = false;
            }
        }
    }

    private static int getResult() {
        int sum = 0;
        for (int i = 1; i < n; i++) {
            sum += Math.abs(selected[i] - selected[i - 1]);
        }
        return sum;
    }
}
