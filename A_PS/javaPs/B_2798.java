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
    static int[] nums;
    static boolean[] visited;
    static int n;
    static int m;
    static int max = Integer.MIN_VALUE;
    static int[] selectedNums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
//        m = Integer.parseInt(st.nextToken());
        nums = new int[n];
        visited = new boolean[n];
        selectedNums = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        dfs(0, 0);
//        System.out.println(max);
    }

    static void dfs(int cnt, int sum) {
        if (cnt == n) {
//            if (sum <= m) {
////                max = Math.max(max, sum);
//            }

            System.out.println(Arrays.toString(selectedNums));
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                selectedNums[cnt] = nums[i];
                dfs(cnt + 1, sum + nums[i]);
                visited[i] = false;
            }
        }
    }
}
