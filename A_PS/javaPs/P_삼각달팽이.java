package javaPs;

public class P_삼각달팽이 {
    public static void main(String[] args) {
        Solution solution = new P_삼각달팽이().new Solution();

        solution.solution(5);
    }
    class Solution {
        public int[] solution(int n) {
            int[] answer = {};
            int[][] graph = new int[n][n];

            int num = 1;
            int x = -1, y = 0;

            for(int i=0; i<n; i++) {
                for (int j=i; j<n; j++) {
                    if (i % 3 == 0) x += 1;
                    else if (i % 3 == 1) y += 1;
                    else if (i % 3 == 2) {
                        x -= 1;
                        y -= 1;
                    }
                    graph[x][y] = num;
                    num++;
                }
            }
            return answer;
        }
    }
}
