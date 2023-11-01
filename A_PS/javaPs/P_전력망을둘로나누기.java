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
        public int solution(int n, int[][] wires) {
            int answer = -1;

            ArrayList<Integer>[] graph = new ArrayList[n+1];

            for(int i=0; i<=n; i++) {
                graph[i] = new ArrayList<>();
            }

            for(int[] wire : wires) {
                int a = wire[0];
                int b = wire[1];

                graph[a].add(b);
                graph[b].add(a);
            }

            return answer;
        }
    }
}
