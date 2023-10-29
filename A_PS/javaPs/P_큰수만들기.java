package javaPs;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class P_큰수만들기 {
    public static void main(String[] args) {
        Solution solution = new P_큰수만들기().new Solution();
        solution.solution("1942", 2);
    }
    class Solution {
        public String solution(String number, int k) {
            String answer = "";
            Queue<Integer> numQ = new LinkedList<>();
            String[] numArr = number.split("");
            Stack<Integer> st = new Stack<>();

            for(String num : numArr) {
                numQ.offer(Integer.valueOf(num));
            }

            st.push(numQ.poll());
            for(int i=1; i<numArr.length; i++) {
                while (!st.isEmpty() && st.peek() < numQ.peek() && k > 0) {
                    st.pop();
                    k--;
                }
                st.push(numQ.poll());
            }

            while (k>0) {
                st.pop();
                k--;
            }


            while (!numQ.isEmpty()) {
                answer += (Integer.toString(numQ.poll()));
            }


            return answer;
        }
    }
}
