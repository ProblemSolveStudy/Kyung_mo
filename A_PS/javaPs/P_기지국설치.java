package javaPs;

public class P_기지국설치 {
    public static void main(String[] args) {
        Solution solution = new P_기지국설치().new Solution();
        solution.solution(11, new int[]{4, 11}, 1);
    }

    class Solution {
        public int solution(int n, int[] stations, int w) {
            int answer = 0;

            // 기지국 전파 범위 2w + 1
            int location = 1;
            int station =0;

            while(location<=n) {
                if(station < stations.length && stations[station] - w <= location) {
                    location = stations[station] + w + 1;
                    station++;
                } else {
                    answer++;
                    location += 2*w+1;
                }
            }

            return answer;
        }
    }
}
