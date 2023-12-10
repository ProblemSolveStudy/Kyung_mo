package javaPs;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.*;
//public class B_2667 {
//    static int n;
//    static List<Integer> nums = new ArrayList<>();
//    static int[][] graph;
//    static boolean[][] visited;
//    static int[] dx = {-1, 1, 0, 0};
//    static int[] dy = {0, 0, -1, 1};
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        n = Integer.parseInt(br.readLine());
//        graph = new int[n][n];
//        visited = new boolean[n][n];
//
//        for (int i = 0; i < n; i++) {
//            String temp = br.readLine();
//            for (int j = 0; j < n; j++) {
//                graph[i][j] = Integer.parseInt(String.valueOf(temp.charAt(j)));
//            }
//        }
//
//        for (int i = 0; i < n; i++) {
//            for (int j = 0; j < n; j++) {
//                if (graph[i][j] == 1) {
//                    bfs(new int[]{i, j});
//                }
//            }
//        }
//
//        System.out.println(nums.size());
//        Collections.sort(nums);
//        for (int i = 0; i < nums.size(); i++) {
//            System.out.println(nums.get(i));
//        }
//    }
//
//    static void bfs(int[] start) {
//        Queue<int[]> q = new LinkedList<>();
//        q.add(start);
//        int cnt=0;
//
//        while (!q.isEmpty()) {
//            int[] temp = q.poll();
//            int x = temp[0];
//            int y = temp[1];
//            visited[x][y] = true;
//            cnt++;
//
//            for (int i = 0; i < 4; i++) {
//                int nx = x + dx[i];
//                int ny = y + dy[i];
//
//                if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && graph[nx][ny] == 1) {
//                    visited[nx][ny] = true;
//                    q.add(new int[]{nx, ny});
//                    graph[nx][ny] = 0;
//                }
//            }
//
//        }
//        nums.add(cnt);
//    }
//}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class B_2667 {
    static int n;
    static int cnt;
    static int[][] graph;
    static boolean[][] visited;
    static ArrayList<Integer> list = new ArrayList<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        visited = new boolean[n][n];
        graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            String temp = br.readLine();
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(String.valueOf(temp.charAt(j)));
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    cnt = 0;
                    dfs(i,j);
                    list.add(cnt);
                }
            }
        }
        System.out.println(list.size());
        Collections.sort(list);
        for (int i : list) {
            System.out.println(i);
        }
    }

    static void dfs(int x, int y) {
        visited[x][y] = true;
        cnt++;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && graph[nx][ny] == 1) {
                dfs(nx, ny);
            }
        }
    }
}