package javaPs;

import java.io.*;
import java.util.*;

public class B_1987 {
    static int R,C;
    static int[][] graph;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean visited[] = new boolean[26];
    static int MAX = Integer.MIN_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        graph = new int[R][C];

        for (int i = 0; i < R; i++) {
            String temp = br.readLine();
            for (int j = 0; j < C; j++) {
                graph[i][j] = temp.charAt(j) - 'A';
            }
        }

        dfs(new int[]{0, 0}, 1);
        System.out.println(MAX);
    }

    static void dfs(int[] start, int cnt) {
        int x = start[0];
        int y = start[1];
        visited[graph[x][y]] = true;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < R && 0 <= ny && ny < C && !visited[graph[nx][ny]]) {
                dfs(new int[]{nx, ny}, cnt+1);
            }
        }
        visited[graph[x][y]] = false;
        MAX = Math.max(MAX, cnt);
    }
}