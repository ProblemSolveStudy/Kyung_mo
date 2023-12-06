package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P_16236 {
    static int n;
    static int[][] graph;

    // 상좌하우
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        StringTokenizer st = null;
        int cur[] = null;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 9) {
                    cur = new int[]{i, j};
                    graph[i][j] = 0;
                }
            }
        }

        int size = 2;
        int eat = 0; // 먹은 물고기 수
        int move = 0; // 움직인 거리

        while(true) {
            PriorityQueue<int[]> q = new PriorityQueue<>((o1, o2) ->
                    o1[2] != o2[2] ? Integer.compare(o1[2], o2[2]) : (o1[0] != o2[0] ? Integer.compare(o1[0], o2[0]) : Integer.compare(o1[1], o2[1]))
            );
            boolean[][] visited = new boolean[n][n];

            q.add(new int[]{cur[0], cur[1], 0});
            visited[cur[0]][cur[1]] = true;

            boolean ck = false;

            while (!q.isEmpty()) {
                cur = q.poll();

                if (graph[cur[0]][cur[1]] != 0 && graph[cur[0]][cur[1]] < size) { // 먹이가 있으면서 상어보다 작다?
                    graph[cur[0]][cur[1]] = 0; // 먹이부분 없애고
                    eat++; // 먹은 수 늘려주고
                    move += cur[2]; //
                    ck = true;
                    break;
                }

                for (int i = 0; i < 4; i++) {
                    int nx = cur[0] + dx[i];
                    int ny = cur[1] + dy[i];

                    if(nx<0 || ny<0 || nx>=n || ny>=n || visited[nx][ny] || graph[nx][ny] > size) continue;

                    q.add(new int[]{nx, ny, cur[2] + 1});
                    visited[nx][ny] = true;
                }
            }

            if(!ck) break;
            if(size == eat) {
                size++;
                eat = 0;
            }
        }
        System.out.println(move);
    }
}