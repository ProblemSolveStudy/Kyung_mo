package javaPs;
import java.util.*;

public class P_줄서는방법 {
    public static void main(String[] args) {
        Solution solution = new P_줄서는방법().new Solution();
        solution.solution(4, 14);
    }
    class Solution {
        public int[] solution(int n, long k) {
            int[] answer = new int[n];

            List<Integer> sequence = new ArrayList<>();
            long totalCase = 1;
            for(int i=0; i<n; i++) {
                sequence.add(i+1);
                totalCase*=i+1;
            }
            k--;
            int idx = 0;
            while (idx < n) {
                totalCase /= n - idx;
                answer[idx++] = sequence.remove((int) (k/totalCase));
                k %= totalCase;

            }
            return answer;
        }
    }
}
