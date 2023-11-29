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
    static int max = Integer.MIN_VALUE;
    static int n;
    static int[] nums;
    static boolean[] visited;
    static int[] selectedNums;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        nums = new int[n];
        visited = new boolean[n];
        selectedNums = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        dfs(0);
        System.out.println(max);
    }

    static void dfs(int cnt) {
        if (cnt == n) {
            max = Math.max(getResult(), max);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                selectedNums[cnt] = nums[i];
                dfs(cnt+1);
                visited[i] = false;
            }
        }
    }

    private static int getResult() {
        int sum = 0;
        for (int i = 1; i < n; i++) {
            sum += Math.abs(selectedNums[i] - selectedNums[i-1]);
        }
        return sum;
    }
}
