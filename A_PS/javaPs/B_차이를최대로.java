package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B_차이를최대로 {
    static int[] nums;
    static boolean[] visited;
    static int[] selected;
    static int n;
    static int result = Integer.MIN_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        String[] temp = br.readLine().split(" ");

        nums = new int[n];
        visited = new boolean[n];
        selected = new int[n];

        for (int i = 0; i < temp.length; i++) {
            nums[i] = Integer.parseInt(temp[i]);
        }
        dfs(0);
        System.out.println(result);
    }
    public static void dfs(int count) {
        if(count == n) {
            result = Math.max(getResult(), result);
        }
        for(int i=0; i<n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                selected[count] = nums[i];
                dfs(count + 1);
                visited[i] = false;
            }
        }
    }
    public static int getResult() {
        int sum = 0;
        for(int i=1; i<n; i++) {
            sum += Math.abs(selected[i] - selected[i - 1]);
        }
        return sum;
    }
}
