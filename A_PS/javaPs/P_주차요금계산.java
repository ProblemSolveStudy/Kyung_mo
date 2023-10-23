package javaPs;

import java.util.*;

public class P_주차요금계산
{
    public static void main(String args[])
    {
        Solution solution = new P_주차요금계산().new Solution();
        System.out.println(solution.solution(new int[]{180, 5000, 10, 600}, new String[]{"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"}));

    }
    class Solution {
        public List<Integer> solution(int[] fees, String[] records) {
    
            List<Integer> answer = new ArrayList<>();        Map<String, Integer> parkingSet = new HashMap<>();
            Map<String, Integer> usingTime = new HashMap<>();
    
            for (int i=0; i<records.length; i++) {
                String[] tempArr = records[i].split(" ");
                String[] splitTime = tempArr[0].split(":");
                int h = Integer.parseInt(splitTime[0]);
                int m = Integer.parseInt(splitTime[1]);
                int time = h*60 +m;
                String carNum = tempArr[1];
                String io = tempArr[2];
    
                if (io.equals("IN")) {
                    parkingSet.put(carNum, time);
                } else {
                    if (usingTime.containsKey(carNum)) {
                        usingTime.put(carNum, usingTime.get(carNum) + time - parkingSet.get(carNum));
                    } else {
                        usingTime.put(carNum, time - parkingSet.get(carNum));
                    }
                    parkingSet.remove(carNum);
                }
            }
    
            if (!parkingSet.isEmpty()) {
                for (Map.Entry<String, Integer> entry : parkingSet.entrySet()) {
                    String carNum = entry.getKey();
                    int time = entry.getValue();
                    if (usingTime.containsKey(carNum)) {
                        usingTime.put(carNum, usingTime.get(carNum) + 1439 - time);
                    } else {
                        usingTime.put(carNum, 1439 - time);
                    }
                }
            }
    
            List<Map.Entry<String, Integer>> sortedList = new ArrayList<>(usingTime.entrySet());
            sortedList.sort(Comparator.comparing(Map.Entry::getKey));
    
            for (Map.Entry<String, Integer> entry : sortedList) {
                int time = entry.getValue();
                int calculatedTime =time - fees[0];
                int extraTime = Math.max(0, (int) Math.ceil((double) calculatedTime / fees[2]));
    
                int cost = fees[1] + extraTime * fees[3];
                answer.add(cost);
            }
    
            return answer;
        }
    }
}
