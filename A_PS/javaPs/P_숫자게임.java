package javaPs;
import java.util.*;

public class P_숫자게임 {
    class Solution {
        public int solution(int[] A, int[] B) {
            int answer = 0;

            Arrays.sort(A);
            Arrays.sort(B);

            int a = 0;
            int b = 0;

            for(int i=0; i<A.length; i++) {
                if (B[b] > A[a]) {
                    b++;
                    a++;
                    answer++;
                } else {
                    b++;
                }
            }
            return answer;
        }
    }
}
