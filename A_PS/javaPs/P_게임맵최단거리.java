package javaPs;

import java.util.*;
public class P_게임맵최단거리
{
    public static void main(String args[])
    {
        Solution solution = new P_게임맵최단거리().new Solution();
        System.out.println(solution.solution(new int[][]{{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1}}));

    }
    class Solution {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        public int solution(int[][] maps) {
            int answer = 0;
            int rows = maps.length;
            int cols = maps[0].length;

            int[][] visited = new int[rows][cols];

            bfs(0, 0, maps, visited);
            answer = visited[rows - 1][cols - 1];

            if (answer == 0) {
                return -1;
            }

            return answer;
        }

        public void bfs(int x, int y, int[][] maps, int[][] visited) {
            Queue<int[]> q = new LinkedList<>();
            q.add(new int[]{x, y});
            visited[x][y] = 1;

            while (!q.isEmpty()) {
                int[] current = q.poll();
                x = current[0];
                y = current[1];

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx < 0 || ny < 0 || nx >= maps.length || ny >= maps[0].length) {
                        continue;
                    }

                    if (visited[nx][ny] == 0 && maps[nx][ny] == 1) {
                        visited[nx][ny] = visited[x][y] + 1;
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }
    }

}
