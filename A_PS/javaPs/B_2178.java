package javaPs;

import java.io.*;
import java.util.*;

public class B_2178 {
    static int n,m;
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
        visited = new boolean[n][m];
        for(int i=0; i<n; i++) {
            String temp = br.readLine();
            for(int j=0; j<m; j++) {
                graph[i][j] = Integer.parseInt(String.valueOf(temp.charAt(j)));
            }
        }

        bfs(new int[]{0, 0});

        System.out.print(graph[n-1][m-1]);
    }
    static void bfs(int[] start) {
        Queue<int[]> q = new LinkedList();
        q.add(start);
        visited[start[0]][start[1]] = true;
        while(!q.isEmpty()) {
            int[] temp = q.poll();
            int x = temp[0];
            int y = temp[1];
            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(0<=nx&&nx<n&&0<=ny&&ny<m&&!visited[nx][ny]&&graph[nx][ny]!=0) {
                    graph[nx][ny] = graph[x][y] + 1;
                    visited[nx][ny] = true;
                    q.add(new int[]{nx,ny});
                }
            }
        }
    }
}