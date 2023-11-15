package javaPs;
import java.util.*;
public class P_네트워크 {
    public static void main(String[] args) {
        Solution solution = new P_네트워크().new Solution();
        solution.solution(3, new int[][]{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}});
    }
    class Solution {
        static boolean[] visited;
        public int solution(int n, int[][] computers) {
            int answer = 0;
            visited = new boolean[n];
            for(int i=0; i<n; i++) {
                if(visited[i] == false) {
                    bfs(i,computers);
                    answer++;
                }
            }
            return answer;
        }

        public void bfs(int start, int[][] computers) {
            Queue<Integer> q = new LinkedList<>();
            q.offer(start);
            visited[start] = true;

            while(!q.isEmpty()) {
                int temp = q.poll();

                for(int i=0; i<computers.length; i++) {
                    if(visited[i] == false && computers[temp][i] == 1) {
                        visited[i] = true;
                        q.offer(i);
                    }
                }

            }
        }
    }
}
