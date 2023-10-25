package javaPs;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class P_롤케이크자르기 {

    public static void main(String[] args) {
        Solution solution = new P_롤케이크자르기().new Solution();

        System.out.println(solution.solution(new int[]{1,2,1,3,1,4,1,2}));
    }


    class Solution {
        public int solution(int[] topping) {
            int answer = 0;

            Map<Integer, Integer> toppings = new HashMap<>();
            Set<Integer> toppingSet = new HashSet<>();

            for(int key : topping) {
                toppings.put(key, toppings.getOrDefault(key, 0) + 1);
            }

            for(int i=0; i<topping.length;i++) {
                toppings.put(topping[i], toppings.get(topping[i]) - 1);

                toppingSet.add(topping[i]);

                if (toppings.get(topping[i]) == 0) toppings.remove(topping[i]);

                if (toppings.size() == toppingSet.size()) answer+=1;
            }

            return answer;
        }
    }
}
