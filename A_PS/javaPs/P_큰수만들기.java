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
            StringBuilder answer = new StringBuilder();

            Stack<Integer> st = new Stack<Integer>();

            Queue<Integer> q = new LinkedList<>();

            String[] temp = number.split("");

            for(String num : temp) {
                q.offer(Integer.valueOf(num));
            }
            st.push(q.poll());

            for(int i=1; i<temp.length; i++) {
                while(!st.isEmpty() && st.peek() < q.peek() && k>0) {
                    st.pop();
                    k--;
                }
                st.push(q.poll());
            }

            while(k>0) {
                st.pop();
                k--;
            }

            while(!st.isEmpty()) {
                answer.append(Integer.toString(st.pop()));
            }

            return answer.reverse().toString();
        }
    }
}
