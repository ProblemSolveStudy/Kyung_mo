package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.StringTokenizer;

public class B_14502 {
    static int n,m;
    static int MAX = Integer.MIN_VALUE;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0);
        System.out.println(MAX);
    }

    static void bfs() {
        Queue<int[]> q = new LinkedList<>();
        int[][] virusMap = new int[n][m];
        visited = new boolean[n][m];
        int cnt =0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                virusMap[i][j] = graph[i][j];
                if(virusMap[i][j] == 2) {
                    q.add(new int[]{i, j});
                }
            }
        }


        while(!q.isEmpty()) {
            int temp[] = q.poll();
            int x = temp[0];
            int y = temp[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m && graph[nx][ny] == 0 && !visited[nx][ny]) {
                    virusMap[nx][ny] = 2;
                    visited[nx][ny] = true;
                    q.add(new int[]{nx, ny});
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (virusMap[i][j] == 0) {
                    cnt++;
                }
            }
        }

        MAX = Math.max(MAX, cnt);
    }

    static void dfs(int cnt) {
        if (cnt == 3) {
            bfs();
            return;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 0) {
                    graph[i][j] = 1;
                    dfs(cnt + 1);
                    graph[i][j] = 0;
                }
            }
        }
    }
}