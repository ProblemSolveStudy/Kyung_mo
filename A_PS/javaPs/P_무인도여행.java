package javaPs;

import java.util.*;

public class P_무인도여행 {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean[][] visited;
    public static void main(String[] args) {
        solution(new String[]{"X591X","X1X5X","X231X", "1XXX1"});
    }


    public static List<Integer> solution(String[] maps) {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();

        visited = new boolean[maps.length][maps[0].length()];
        String[][] graph = new String[maps.length][maps[0].length()];


        for(int i=0; i<maps.length; i++) {
            graph[i] =  maps[i].split("");
        }

        System.out.println(Arrays.deepToString(graph));

        for(int i=0; i<maps.length; i++) {
            for(int j=0; j<maps[0].length(); j++) {
                if(!graph[i][j].equals("X") && !visited[i][j]) {
                    list.add(bfs(graph, i, j));
                }
            }
        }

        if(list.isEmpty()) list.add(-1);
        Collections.sort(list);



        return list;
    }

    public static int bfs(String[][] graph,int x,int y) {
        Queue<int[]> q = new LinkedList<>();
        int cnt=0;
        q.offer(new int[]{x,y});
        visited[x][y] = true;

        while (!q.isEmpty()) {
            int[] polled = q.poll();
            x = polled[0];
            y = polled[1];
            cnt += Integer.parseInt(graph[x][y]);

            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx<0 || ny<0 || nx >= graph.length || ny >= graph[0].length) continue;
                if (!visited[nx][ny] && !graph[nx][ny].equals("X")) {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
        return cnt;
    }
}
