package javaPs;

import java.util.*;
import java.io.*;

public class P_14889 {
    static int[][] graph;
    static int n;
    static boolean[] visited;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dfs(0, 0);
        System.out.println(min);
    }

    public static void dfs(int idx, int depth) {
        if (depth == n / 2) {
            getResult();
            return;
        }

        for(int i=idx; i<n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(i + 1, depth + 1);
                visited[i] = false;
            }
        }
    }

    public static void getResult() {
        int start = 0;
        int link = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (visited[i] && visited[j]) {
                    start += graph[i][j] + graph[j][i];
                } else if (!visited[i] && !visited[j]) {
                    link += graph[i][j] + graph[j][i];
                }
            }
        }

        int temp = Math.abs(start - link);
        min = Math.min(min, temp);
    }
}
