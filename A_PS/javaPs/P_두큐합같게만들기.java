package javaPs;

import java.util.*;
class P_두큐합같게만들기 {
    public int solution(int[] queue1, int[] queue2) {
        int answer = -2;
        Queue<Long> q1 = new LinkedList<>();
        Queue<Long> q2 = new LinkedList<>();
        long qSum = 0;
        long q1Sum = 0;
        long q2Sum = 0;

        for(int i=0; i<queue1.length; i++) {
            q1.offer(Long.valueOf(queue1[i]));
            q2.offer(Long.valueOf(queue2[i]));
        }

        for(int i=0; i<queue1.length; i++) {
            q1Sum += queue1[i];
            q2Sum += queue2[i];
        }

        qSum = q1Sum + q2Sum;

        if (qSum % 2 == 1) return -1;

        int cnt = 0;
        while (true) {
            if (q1Sum == q2Sum) return cnt;

            if (q1Sum > q2Sum) {
                long temp = q1.poll();
                q1Sum -= temp;
                q2Sum += temp;
                q2.offer(temp);
            } else if (q1Sum < q2Sum) {
                long temp = q2.poll();
                q1Sum += temp;
                q2Sum -= temp;
                q1.offer(temp);
            } else {
                return -1;
            }

            if (cnt > (queue1.length + queue2.length) * 3) return -1;
            cnt++;
        }
    }
}