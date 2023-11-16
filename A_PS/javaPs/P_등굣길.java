package javaPs;
public class P_등굣길 {
    public static void main(String[] args) {
        Solution solution = new P_등굣길().new Solution();
        solution.solution(4, 3, new int[][]{{2, 2}});
    }
    class Solution {
        public int solution(int m, int n, int[][] puddles) {
            int answer = 0;
            int[][] graph = new int[n][m];

            for(int[] puddle : puddles) {
                int x = puddle[0];
                int y = puddle[1];

                graph[x-1][y-1] = -1;
            }

            graph[0][0] = 1;

            for(int i=0; i<n; i++) {
                for(int j=0; j<m; j++) {

                    if(graph[i][j]== -1) {
                        graph[i][j] = 0;
                        continue;
                    }

                    if(!(i==0 && j==0)) {
                        int left = 0;
                        int up = 0;

                        if(j>0) left = graph[i][j-1];
                        if(i>0) up = graph[i-1][j];

                        graph[i][j] = (left + up) % 1000000007;
                    }
                }
            }
            return graph[n-1][m-1];
        }
    }
}
