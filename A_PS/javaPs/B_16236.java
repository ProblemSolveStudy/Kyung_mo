package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B_16236 {
    static int n;
    static int graph[][];
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[] now;
    static int size;
    static int eat;
    static int move;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 9) {
                    graph[i][j] = 0;
                    now = new int[]{i, j};
                }
            }
        }
        size = 2;
        eat = 0;
        move = 0;

        while (true) {
            PriorityQueue<int[]> q = new PriorityQueue<>((o1, o2) ->
                    o1[2] != o2[2] ? Integer.compare(o1[2], o2[2]) : (o1[0] != o2[0] ? Integer.compare(o1[0], o2[0]) : Integer.compare(o1[1], o2[1])));

            boolean[][] visited = new boolean[n][n];
            boolean ck = false;
            q.add(new int[]{now[0], now[1], 0});
            visited[now[0]][now[1]] = true;

            while (!q.isEmpty()) {
                now = q.poll();
                int x = now[0];
                int y = now[1];
                int sharkMove = now[2];

                if(graph[x][y] != 0 && graph[x][y] < size) {
                    graph[x][y] = 0;
                    eat++;
                    move += sharkMove;
                    ck = true;
                    break;
                }

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && graph[nx][ny] <= size) {
                        q.add(new int[]{nx, ny, sharkMove + 1});
                        visited[nx][ny] = true;
                    }
                }
            }
            if(eat==size) {
                size++;
                eat=0;
            }
            if(!ck) break;
        }
        System.out.println(move);
    }
}