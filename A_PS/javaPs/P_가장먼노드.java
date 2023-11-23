package javaPs;

import java.util.*;
public class P_가장먼노드 {
    class Solution {
//        static List<List<Integer>> graph = new ArrayList<>();
//        static int[] visited;
//        static int depth = 0;
//        public int solution(int n, int[][] edge) {
//            int answer = 0;
//            visited = new int[n+1];
//
//            for(int i=0; i<=n; i++) graph.add(new ArrayList<>());
//
//            for(int[] temp : edge) {
//                int a = temp[0];
//                int b = temp[1];
//                graph.get(a).add(b);
//                graph.get(b).add(a);
//            }
//
//            bfs();
//
//            for(int i=1; i<=n; i++) {
//                if(depth == visited[i]) answer++;
//            }
//            return answer;
//        }
//
//        public void bfs() {
//            Queue<int[]> q = new LinkedList<>();
//            q.add(new int[]{1,1});
//            visited[1] = 1;
//
//
//            while(!q.isEmpty()) {
//                int[] temp = q.poll();
//                int node = temp[0];
//                int cnt = temp[1];
//
//                if(depth < cnt) depth = cnt;
//                for(int i=0; i<graph.get(node).size(); i++) {
//                    int a = graph.get(node).get(i);
//
//                    if(visited[a] == 0) {
//                        visited[a] = cnt+1;
//                        q.add(new int[]{a, cnt+1});
//                    }
//                }
//            }
//        }

        static List<Integer>[] graph;
        public int solution(int n, int[][] edge) {
            graph = new ArrayList[n+1];
            int answer = 0;


            return answer;
        }
    }
}
