package javaPs;
import java.util.*;
public class P_이중우선순위큐 {
    public static void main(String[] args) {
        Solution solution = new P_이중우선순위큐().new Solution();
    }

    class Solution {
        public int[] solution(String[] operations) {
            int[] answer = {};
            PriorityQueue<Integer> q = new PriorityQueue<>(Comparator.reverseOrder());

            for(String s : operations) {
                String[] temp = s.split(" ");
                String command = temp[0];
                String num = temp[1];

                if (command.equals("|")) {
                    if (num.equals("1")) {

                    }
                    q.offer(Integer.valueOf(num));
                } else if (command.equals("D")){

                }
            }
            return answer;
        }
    }
}
