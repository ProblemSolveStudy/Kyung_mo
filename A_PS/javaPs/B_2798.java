package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 3개의 원소 조합 중 가장 값이 근사값인 조합을 구해서 합을 구하면 될듯?
 */
public class B_2798 {
    static int n,m,max;
    static int[] arr, selected;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        visited = new boolean[n];
        max = Integer.MIN_VALUE;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        backTracking(0, 0);
        System.out.println(max);
    }

    private static void backTracking(int cnt, int sum) {
        if(cnt == 3) {
            if (sum <= m) {
                max = Math.max(max, sum);
            }
            return;
        }
        for (int i = cnt; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                backTracking(cnt + 1, sum + arr[i]);
                visited[i] = false;
            }
        }
    }
}
