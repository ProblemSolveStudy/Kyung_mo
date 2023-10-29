package javaPs;

import java.util.LinkedList;
import java.util.Queue;

public class P_두큐합같게만들기 {
    public static void main(String[] args) {
        Solution solution = new P_두큐합같게만들기().new Solution();
        System.out.println(solution.solution(new int[]{3, 2, 7, 2}, new int[]{4, 6, 5, 1}));


    }

    class Solution {
        public long solution(int[] queue1, int[] queue2) {
            long answer = -2;
            long qSum = 0;
            long q1Sum = 0;
            long q2Sum = 0;

            Queue<Long> q1 = new LinkedList<>();
            Queue<Long> q2 = new LinkedList<>();

            for(int i=0; i<queue1.length; i++) {
                q1.offer((long) queue1[i]);
                q2.offer((long) queue2[i]);
            }

            for (int i=0; i<queue1.length; i++) {
                q1Sum += queue1[i];
                q2Sum += queue2[i];
            }

            if (qSum % 2 == 1) return -1;

            long cnt = 0;
            while (true) {
                if (q1Sum == q2Sum) return cnt;

                if (q1Sum > q2Sum) {
                    long temp = q1.poll();
                    q2.offer(temp);
                    q1Sum-=temp;
                    q2Sum+=temp;
                } else {
                    long temp = q2.poll();
                    q1.offer(temp);
                    q1Sum+=temp;
                    q2Sum-=temp;
                }
                cnt++;
            }
        }
    }
}
