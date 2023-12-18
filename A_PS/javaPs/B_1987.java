package javaPs;

import java.io.*;
import java.util.*;

public class B_1987 {
    static int r,c;
    static boolean[] visited = new boolean[26];
    static int[][] graph;
    static int MAX = Integer.MIN_VALUE;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        graph = new int[r][c];

        for (int i = 0; i < r; i++) {
            String temp = br.readLine();
            for (int j = 0; j < c; j++) {
                graph[i][j] = temp.charAt(j) - 'A';
            }
        }
        dfs(0,0,1);
        System.out.println(MAX);
    }

    static void dfs(int x, int y, int cnt) {
        visited[graph[x][y]] = true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < r && ny < c && 0 <= ny && !visited[graph[nx][ny]]) {
                dfs(nx, ny, cnt + 1);
            }
        }
        visited[graph[x][y]] = false;
        MAX = Math.max(MAX, cnt);
    }
}