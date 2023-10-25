package javaPs;

import java.util.Arrays;
import java.util.Stack;

public class P_뒤에있는큰수찾기 {
    public static void main(String[] args) {
        Solution solution = new P_뒤에있는큰수찾기().new Solution();

        System.out.println(solution.solution(new int[]{2,3,3,5}));
    }

    class Solution {
        public int[] solution(int[] numbers) {
            int[] answer = new int[numbers.length];

            Stack<Integer> st = new Stack<>();

            st.push(0);

            for(int i=1; i< numbers.length; i++) {
                while (!st.isEmpty() && numbers[st.peek()] < numbers[i]) {
                    answer[st.pop()] = numbers[i];
                }

                st.push(i);
            }

            while(!st.isEmpty()) answer[st.pop()] = -1;


            return answer;
        }
    }
}
