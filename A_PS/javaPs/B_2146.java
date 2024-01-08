package javaPs;

import java.util.*;
import java.io.*;

public class B_2146 {
    static int n;
    static int MIN = Integer.MAX_VALUE;
    static int[][] graph;
    static int[][] cloneMap;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int num = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    dfs(new int[]{i, j}, num);
                    num++;
                }
            }
        }

        for (int i = 1; i < num; i++) {
            bfs(i);
        }

        System.out.println(MIN);
    }

    static void bfs(int num) {
        Queue<int[]> q = new LinkedList<>();
        cloneMap = new int[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cloneMap[i][j] = graph[i][j];
                if (cloneMap[i][j] == num) {
                    q.add(new int[]{i, j, 0});
                    visited[i][j] = true;
                }
            }
        }

        while (!q.isEmpty()) {
            int[] temp = q.poll();
            int x= temp[0];
            int y = temp[1];
            int move = temp[2];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny]) {
                    if (cloneMap[nx][ny] != num && cloneMap[nx][ny] != 0) {
                        MIN = Math.min(MIN, move);
                    }
                    if (cloneMap[nx][ny] == 0) {
                        q.add(new int[]{nx, ny, move + 1});
                        visited[nx][ny] = true;
                    }
                }
            }
        }
    }

    static void dfs(int[] start, int num) {
        int x = start[0];
        int y = start[1];

        visited[x][y] = true;
        graph[x][y] = num;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && graph[nx][ny] == 1) {
                dfs(new int[]{nx, ny}, num);
            }
        }
    }
}