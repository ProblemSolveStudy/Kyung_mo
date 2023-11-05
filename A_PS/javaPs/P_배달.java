package javaPs;

public class P_배달 {
    class Solution {
        static final int INF = 500_000;
        public int solution(int N, int[][] road, int K) {
            int answer = 0;

            int[][] map = new int[N][N];

            for(int i=0; i<N; i++) {
                for (int j=0; j<N; j++) {
                    if (i==j) {
                        continue;
                    }
                    map[i][j] = INF;
                }
            }

            for(int[] data : road) {
                map[data[0] - 1][data[1] - 1] = Math.min(map[data[0] - 1][data[1] - 1], data[2]);
                map[data[1] - 1][data[0] - 1] = Math.min(map[data[1] - 1][data[0] - 1], data[2]);
            }

            for(int k=0; k<N; k++) {
                for(int i=0; i<N; i++) {
                    for(int j=0; j<N; j++) {
                        map[i][j] = Math.min(map[i][j], map[i][k] + map[k][j]);
                    }
                }
            }

            for(int i=0; i<map[0].length; i++) {
                if (map[0][i] <= K) {
                    answer++;
                }
            }
            return answer;
        }
    }
}
