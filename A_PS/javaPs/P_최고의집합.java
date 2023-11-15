package javaPs;

import java.util.*;
public class P_최고의집합 {
    class Solution {
        public int[] solution(int n, int s) {
            int[] answer = new int[n];

            if(n > s) return new int[]{-1};

            for(int i=0; i<n; i++) {
                answer[i] = s/n;
            }

            for(int i=0; i<s%n; i++) {
                answer[i]++;
            }
            Arrays.sort(answer);
            return answer;
        }
    }
}
