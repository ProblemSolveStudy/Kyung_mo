package javaPs;

import java.util.*;

public class P_메뉴리뉴얼 {
    public static void main(String[] args) {
        Solution solution = new P_메뉴리뉴얼().new Solution();
        solution.solution(new String[]{"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"}, new int[]{2, 3, 4});
    }
    class Solution {
        static Map<String, Integer> map;
        public List<String> solution(String[] orders, int[] course) {
            List<String> answer = new ArrayList<>();

            for(int i=0; i<orders.length; i++) {
                char[] charArr = orders[i].toCharArray();
                Arrays.sort(charArr);
                orders[i] = String.valueOf(charArr);
            }

            // course의 길이만큼 반복하면서 조합의 개수를 구함
            for(int i=0; i<course.length; i++) {
                map = new HashMap<>();
                int max = Integer.MIN_VALUE;

                for(int j=0; j<orders.length; j++) {
                    StringBuilder sb = new StringBuilder();
                    if (course[i] <= orders[j].length()) {
                        combi(orders[j], sb, 0, 0, course[i]);
                    }
                }

                for(Map.Entry<String,Integer> entry : map.entrySet()) {
                    max = Math.max(max, entry.getValue());
                }

                for(Map.Entry<String, Integer> entry : map.entrySet()) {
                    if(max >= 2 && entry.getValue() == max)
                        answer.add(entry.getKey());
                }
            }
            Collections.sort(answer);

            return answer;
        }

        // 메뉴 구성, sb, 조합 인덱스, 코스요리 개수 종료조건
        public static void combi(String str, StringBuilder sb, int idx, int cnt, int n) {
            if(cnt == n) {
                map.put(sb.toString(), map.getOrDefault(sb.toString(),0) + 1);
                return;
            }
            for (int i=idx; i<str.length(); i++) {
                sb.append(str.charAt(i));
                combi(str,sb,i+1,cnt+1,n);
                sb.delete(cnt,cnt+1);
            }
        }
    }
}
