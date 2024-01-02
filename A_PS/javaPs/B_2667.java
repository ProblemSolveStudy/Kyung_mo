package javaPs;

import java.io.*;
import java.util.*;

public class B_2667 {
    static int n;
    static int[][] graph;
    static boolean[][] visited;
    static List<Integer> result = new ArrayList<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int cnt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            String temp = br.readLine();
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(String.valueOf(temp.charAt(j)));
            }
        }


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1) {
                    cnt=0;
                    dfs(new int[]{i, j});
                    result.add(cnt);
                }
            }
        }

        Collections.sort(result);
        System.out.println(result.size());
        for(int i : result) {
            System.out.println(i);
        }
    }
    static void dfs(int[] start) {
        int x = start[0];
        int y = start[1];
        visited[x][y]=true;
        cnt++;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && graph[nx][ny] == 1) {
                graph[nx][ny] = 0;
                dfs(new int[]{nx, ny});
            }
        }
    }
}