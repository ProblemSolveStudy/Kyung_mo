package javaPs;

import java.util.Arrays;

public class P_주식가격 {
    public static void main(String[] args) {
        Solution solution = new P_주식가격().new Solution();
        System.out.println(Arrays.toString(solution.solution(new int[]{1,2,3,2,3})));
    }

    class Solution {
        public int[] solution(int[] prices) {
            int[] answer = new int[prices.length];
            
            for (int i=0; i<prices.length; i++) {
                for (int j=i+1; j<prices.length; j++) {
                    if (prices[i] > prices[j]) {
                        answer[i]++;
                        break;
                    }
                    answer[i]++;
                }
            }
            return answer;
        }
    }
}
