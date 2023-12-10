package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B_10026 {
    static int n;
    static String[][] graph;
    static String[][] colorGraph;
    static boolean[][] visited;
    static boolean[][] cVisited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        graph = new String[n][n];
        colorGraph = new String[n][n];
        visited = new boolean[n][n];
        cVisited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            String temp = br.readLine();
            for (int j = 0; j < n; j++) {
                graph[i][j] = String.valueOf(temp.charAt(j));

                colorGraph[i][j] = String.valueOf(temp.charAt(j));
                if (String.valueOf(temp.charAt(j)).equals("G")) {
                    colorGraph[i][j] = "R";
                }
            }
        }

        int normalCnt = 0;
        int colorCnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                String normalNow = graph[i][j];
                String colorNow = colorGraph[i][j];
                if (normalNow.equals(graph[i][j]) && !visited[i][j]) {
                    dfs(i, j, normalNow, graph, visited);
                    normalCnt++;
                }
                if (colorNow.equals(colorGraph[i][j]) && !cVisited[i][j]) {
                    dfs(i, j, colorNow, colorGraph, cVisited);
                    colorCnt++;
                }

            }
        }
        System.out.print(normalCnt + " ");
        System.out.println(colorCnt);
    }

    static void dfs(int x, int y, String color, String[][] graph, boolean[][] visited) {
        visited[x][y] = true;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && graph[nx][ny].equals(color)) {
                dfs(nx, ny, color, graph, visited);
            }
        }
    }
}
