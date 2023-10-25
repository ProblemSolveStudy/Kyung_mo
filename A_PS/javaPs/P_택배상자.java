package javaPs;
import java.util.*;

public class P_택배상자 {
    public static void main(String[] args) {
        Solution solution = new P_택배상자().new Solution();

        solution.solution(new int[]{4, 3, 1, 2, 5});
    }
    class Solution {
        public int solution(int[] order) {
            int answer = 0;

            int[] priority = new int[order.length]; // 각 요소의 인덱스

            for(int i=0; i<order.length; i++) {
                priority[order[i]-1] = i;
            }

            Stack<Integer> stack = new Stack<>();

            int target = 0;

            for(int i=0; i<priority.length; i++) {
                if(priority[i] == target) target++;
                else stack.push(priority[i]);

                while(!stack.isEmpty() && stack.peek() == target) {
                    stack.pop();
                    target++;
                }
            }


            return target;
        }
    }
}
