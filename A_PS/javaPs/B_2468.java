package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_2468 {
    static int n;
    static int MAX = Integer.MIN_VALUE;
    static int[][] graph;
    static boolean[][] visited;
    static int cnt = 0;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] > MAX) {
                    MAX = graph[i][j];
                }
            }
        }

        int max = 0;
        for (int height = 0; height < MAX + 1; height++) {
            visited = new boolean[n][n];
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (graph[i][j] > height && !visited[i][j]) {
                        dfs(i, j, height);
                        cnt++;
                    }
                }
            }
            max = Math.max(cnt, max);
        }
        System.out.println(max);
    }

    static void dfs(int x, int y, int height) {
        visited[x][y] = true;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && graph[nx][ny] > height) {
                dfs(nx, ny, height);
            }
        }
    }
}
