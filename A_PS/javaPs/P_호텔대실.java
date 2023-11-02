package javaPs;

import java.util.*;
public class P_호텔대실 {
    class Solution {
        public int solution(String[][] book_time) {
            int answer = 0;
            int[][] intBookTime = new int[book_time.length][2];

            for(int i=0; i<book_time.length; i++) {
                intBookTime[i][0] = Integer.parseInt(book_time[i][0].replace(":", ""));
                intBookTime[i][1] = Integer.parseInt(book_time[i][1].replace(":", ""));

                intBookTime[i][1] += 10;

                if (intBookTime[i][1] % 100 >= 60) intBookTime[i][1] += 40;
            }

            Arrays.sort(intBookTime, (a, b) -> {
                if (a[0] > b[0]) return 1;
                else if (a[0] < b[0]) return -1;
                else {
                    if(a[1] > b[1]) return 1;
                    else return -1;
                }
            });

            PriorityQueue<Integer> q = new PriorityQueue<>();

            q.offer(intBookTime[0][1]);

            for(int i=1; i<intBookTime.length; i++) {
                if(q.peek() > intBookTime[i][0]) q.offer(intBookTime[i][1]);
                else {
                    q.poll();
                    q.offer(intBookTime[i][1]);
                }
            }
            return q.size();
        }
    }
}
