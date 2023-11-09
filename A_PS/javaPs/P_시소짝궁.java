package javaPs;

import java.util.*;
public class P_시소짝궁 {
    class Solution {
        public long solution(int[] weights) {
            long answer = 0;
            Map<Double, Long> map = new HashMap<>();

            for (long i : weights) {
                map.put((1.0 * i), map.getOrDefault((1.0 * i), 0L) + 1);
            }
            for (Double i : map.keySet()) {
                if (map.get(i) > 1) {
                    answer += (long) ((map.get(i) * (map.get(i) - 1)) / 2);
                }
                if (map.containsKey(i * (1.0 / 2))) {
                    answer += (long) (map.get(i) * (map.get(i * (1.0 / 2))));
                }
                if (map.containsKey(i * (2.0 / 3))) {
                    answer += (long) (map.get(i) * (map.get(i * (2.0 / 3))));
                }
                if (map.containsKey(i * (3.0 / 4))) {
                    answer += (long) (map.get(i) * (map.get(i * (3.0 / 4))));
                }
            }

            return answer;
        }
    }
}