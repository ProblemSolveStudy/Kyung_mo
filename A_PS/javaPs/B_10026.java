package javaPs;

import java.io.IOException;
import java.io.*;
import java.util.*;

public class B_10026 {
    static int n;
    static String[][] graph;
    static String[][] abnormalGraph;
    static boolean[][] visited;
    static boolean[][] abnormalVisited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        graph = new String[n][n];
        abnormalGraph = new String[n][n];

        visited = new boolean[n][n];
        abnormalVisited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            String temp = br.readLine();
            for (int j = 0; j < n; j++) {
                String s = String.valueOf(temp.charAt(j));
                graph[i][j] = s;
                abnormalGraph[i][j] = s;
                if (s.equals("R")) {
                    abnormalGraph[i][j] = "G";
                }
            }
        }

        int normalCnt = 0;
        int abnormalCnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                String normalColor = graph[i][j];
                String abnormalColor = abnormalGraph[i][j];

                if (normalColor.equals(graph[i][j]) && !visited[i][j]) {
                    dfs(graph, visited, new int[]{i, j});
                    normalCnt++;
                }
                if (abnormalColor.equals(abnormalGraph[i][j]) && !abnormalVisited[i][j]) {
                    dfs(abnormalGraph, abnormalVisited, new int[]{i, j});
                    abnormalCnt++;
                }
            }
        }
        System.out.println(normalCnt + " " + abnormalCnt);
    }
    static void dfs(String[][] graph, boolean[][] visited, int[] start) {
        visited[start[0]][start[1]] = true;

        for (int i = 0; i < 4; i++) {
            int nx = start[0] + dx[i];
            int ny = start[1] + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && graph[nx][ny].equals(graph[start[0]][start[1]])) {
                dfs(graph, visited, new int[]{nx, ny});
            }
        }
    }
}