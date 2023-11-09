package javaPs;
import java.util.*;
import java.io.*;

public class B_14502 {
    static int N,M;
    static int max = Integer.MIN_VALUE;
    static int[][] graph;
    static int[][] virusMap;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new int[N][M];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dfs(0);
        System.out.print(max);
    }
    public static void dfs(int wall) {
        if(wall == 3) {
            bfs();
            return;
        }
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                if (graph[i][j] == 0) {
                    graph[i][j] = 1;
                    dfs(wall+1);
                    graph[i][j] = 0;
                }
            }
        }
    }

    public static void bfs() {
        Queue<int[]> q = new LinkedList<>();
        virusMap = new int[N][M];
        int cnt =0;
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                virusMap[i][j] = graph[i][j];
                if(virusMap[i][j] == 2) q.add(new int[]{i,j});
            }
        }

        while (!q.isEmpty()) {
            int[] temp = q.poll();
            int x = temp[0];
            int y = temp[1];

            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0<=nx && nx<N && 0<=ny && ny<M && virusMap[nx][ny] == 0) {
                    virusMap[nx][ny] = 2;
                    q.add(new int[]{nx,ny});
                }
            }
        }
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                if(virusMap[i][j] == 0) cnt++;
            }
        }
        max = Math.max(max, cnt);
    }
}
//public class B_14502 {
//    static int n,m;
//    static int[][] graph;
//    static int[][] virusMap;
//    static int[] dx = {-1, 1, 0, 0};
//    static int[] dy = {0, 0, -1, 1};
//    static int max = Integer.MIN_VALUE;
//    public static void main(String[] args) throws IOException {
//        // 벽 3개 세우기 가능
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//
//        n = Integer.parseInt(st.nextToken());
//        m = Integer.parseInt(st.nextToken());
//
//        graph = new int[n][m];
//        for(int i=0; i<n; i++) {
//            st = new StringTokenizer(br.readLine());
//            for(int j=0; j<m; j++) {
//                graph[i][j] = Integer.parseInt(st.nextToken());
//            }
//        }
//
//        dfs(0);
//
//        System.out.println(max);
//    }
//
//    public static void dfs(int wall) {
//        if (wall == 3) {
//            bfs();
//            return;
//        }
//        for(int i=0; i<n; i++) {
//            for(int j=0; j<m; j++) {
//                if (graph[i][j] == 0) {
//                    graph[i][j] = 1;
//                    dfs(wall+1);
//                    graph[i][j] = 0;
//                }
//            }
//        }
//    }
//
//    public static void bfs() {
//        Queue<int[]> q = new LinkedList<>();
//        virusMap = new int[n][m];
//
//        for(int i=0; i<n; i++) {
//            for(int j=0; j<m; j++) {
//                virusMap[i][j] = graph[i][j];
//                if(virusMap[i][j] == 2) q.add(new int[]{i, j});
//            }
//        }
//
//        while (!q.isEmpty()) {
//            int[] start = q.poll();
//            int x = start[0];
//            int y = start[1];
//
//            for(int i=0; i<4; i++) {
//                int nx = x + dx[i];
//                int ny = y + dy[i];
//
//                if(0<=nx && nx<n && 0<=ny && ny<m && virusMap[nx][ny] == 0) {
//                    virusMap[nx][ny] = 2;
//                    q.add(new int[]{nx, ny});
//                }
//            }
//        }
//        int cnt =0;
//        for(int i=0; i<n; i++) {
//            for(int j=0; j<m; j++) {
//                if (virusMap[i][j] == 0) cnt++;
//            }
//        }
//        max = Math.max(max, cnt);
//    }
//
//}

