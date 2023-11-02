package javaPs;
import java.util.*;

public class P_전력망을둘로나누기 {
    public static void main(String[] args) {
        Solution solution = new P_전력망을둘로나누기().new Solution();
        int[][] wires =  {
                {1, 3},
                {2, 3},
                {3, 4},
                {4, 5},
                {4, 6},
                {4, 7},
                {7, 8},
                {7, 9}
        };
        solution.solution(9, wires);

    }
    class Solution {
        static ArrayList<Integer>[] graph;
        public int solution(int n, int[][] wires) {
            int answer = -1;
            graph = new ArrayList[n+1];
            for(int i=0; i<=n; i++) {
                graph[i] = new ArrayList<>();
            }
            for(int[] wire : wires) {
                int a = wire[0];
                int b = wire[1];

                graph[a].add(b);
                graph[b].add(a);
            }
            int min = Integer.MAX_VALUE;

            for(int[] wire: wires) {
                int a = wire[0];
                int b = wire[1];

                graph[a].remove(Integer.valueOf(b));
                graph[b].remove(Integer.valueOf(a));

                min = Math.min(min, Math.abs(bfs(a) - bfs(b)));

                graph[a].add(b);
                graph[b].add(a);
            }

            // System.out.println(Arrays.toString(graph));
            return min;
        }
        int bfs(int start) {
            Queue<Integer> q = new LinkedList<>();
            q.offer(start);

            boolean[] visited = new boolean[graph.length];
            int cnt =1;
            while (!q.isEmpty()) {
                int s = q.poll();
                visited[s] = true;
                List<Integer> temp = graph[s];
                for(Integer num : temp) {
                    if (!visited[num]) {
                        q.offer(num);
                        cnt++;
                    }
                }
            }
            return cnt;
        }
    }
}
