package javaPs;

import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

public class P_다리를지나는트럭 {
    public static void main(String[] args) {
        Solution solution = new P_다리를지나는트럭().new Solution();
        solution.solution(2, 10, new int[]{7, 4, 5, 6});
    }
    class Solution {
        public int solution(int bridge_length, int weight, int[] truck_weights) {
            int answer = 0;

            Queue<Integer> bridge = new LinkedList<>();
            Queue<Integer> truckQ = new LinkedList<>();

            for(int num : truck_weights) {
                truckQ.offer(num);
            }

            for (int i=0; i<bridge_length; i++) {
                bridge.add(0);
            }

            int time = 0;
            int sumTrucks = 0;

            while (!truckQ.isEmpty()){
                sumTrucks += truckQ.peek();

                if (sumTrucks <= weight) bridge.add(truckQ.poll());
                else {
                    sumTrucks -= truckQ.peek();
                    bridge.add(0);
                }
                time++;
                sumTrucks -= bridge.poll();
            }


            return time + bridge_length;
        }
    }
}
