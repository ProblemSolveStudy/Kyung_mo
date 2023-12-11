package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B_1987 {
    static int r,c;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[][] graph;
    static boolean[] visited = new boolean[26];
    static int max = Integer.MIN_VALUE;
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

        dfs(0, 0, 0);
        System.out.println(max);
    }

    static void dfs(int x, int y, int cnt) {

        if (visited[graph[x][y]]) {
            max = Math.max(max, cnt);
            return;
        }

        visited[graph[x][y]] = true;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < r && 0 <= ny && ny < c) {
                dfs(nx, ny, cnt + 1);
            }
        }

        visited[graph[x][y]] = false;
    }
}