package javaPs;
import java.util.*;
public class P_시소짝궁 {
    public static void main(String[] args) {
        Solution solution = new P_시소짝궁().new Solution();
        solution.solution(new int[]{100,180,360,100,270});
    }
    class Solution {
        public long solution(int[] weights) {
            long answer = 0;
            Map<Double, Integer> map = new HashMap<>();
            for(int i : weights) {
                map.put((1.0 * i), map.getOrDefault((i*1.0), 0) + 1);
            }
            for(Double i : map.keySet()) {
                double a = i*1.0;
                double b = (i*2.0)/3.0;
                double c = (i*1.0)/2.0;
                double d = (i*3.0)/4.0;
                if(map.containsKey(a)) answer += map.get(a);
                if(map.containsKey(b)) answer += map.get(b);
                if(map.containsKey(c)) answer += map.get(c);
                if(map.containsKey(d)) answer += map.get(d);
            }

            return answer;
        }
    }

}
