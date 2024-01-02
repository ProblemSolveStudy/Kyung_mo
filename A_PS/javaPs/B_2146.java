package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B_2146 {
    static int[][] graph;
    static int[][] cloneGraph;
    static boolean[][] visited;
    static int n;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int MIN = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        cloneGraph = new int[n][n];
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
                    dfs(i,j, num);
                    num++;
                }
            }
        }

        for (int i = 1; i < num; i++) {
            cloneGraph = new int[n][n];
            for (int j = 0; j < n; j++) {
                cloneGraph[j] = Arrays.copyOf(graph[j], n);
            }

            bfs(i);
        }

        System.out.println(MIN);
    }

    static void bfs(int num) {
        Queue<int[]> q = new LinkedList<>();
        boolean[][] ck = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(cloneGraph[i][j] == num) {
                    q.add(new int[]{i, j, 0});
                    ck[i][j] = true;
                }
            }
        }

        while (!q.isEmpty()) {
            int[] temp = q.poll();
            int x = temp[0];
            int y = temp[1];
            int move = temp[2];


            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];


                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if (cloneGraph[nx][ny] != num && cloneGraph[nx][ny] != 0) {
                        MIN = Math.min(MIN, move);
                    }
                    if(!ck[nx][ny] && cloneGraph[nx][ny] == 0) {
                        q.add(new int[]{nx, ny, move+1});
                        ck[nx][ny] = true;
                    }
                }
            }
        }
    }

    static void dfs(int x, int y, int num) {
        visited[x][y] = true;
        graph[x][y] = num;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && graph[nx][ny] ==1) {
                dfs(nx, ny, num);
            }
        }
    }
}
