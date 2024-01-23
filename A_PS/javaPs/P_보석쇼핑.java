package javaPs;
import java.util.*;
import java.util.*;

/*
생각나는 알고리즘 : 투포인터 (앞에서부터 정렫뢴 보석들에서 숫자를 하나씩 줄여나가는 방식으로 최대 size개수를 구하면 될 듯?)
1. map : 지금까지 무지가 선택한 보석의 개수
2. set : gems 목록

투포인터로 진행하면서 right 값을 하나씩 늘린 후??????????????//

*/
class Solution {
    static Set<String> set = new HashSet<>();
    static Map<String, Integer> map = new HashMap<>();

    static int min = Integer.MAX_VALUE;

    public int[] solution(String[] gems) {
        int[] answer = new int[2];

        for (String gem : gems) {
            set.add(gem);
        }

        int left = 0; // start
        int right = 0; // end

        while(true) {
            if (map.size() == set.size()) {
                map.put(gems[left], map.get(gems[left]) - 1);
                if(map.get(gems[left]) == 0) {
                    map.remove(gems[left]);
                }
                left++;

            } else if (right == gems.length) {
                break;
            } else {
                map.put(gems[right], map.getOrDefault(gems[right], 0) + 1);
                right++;
            }

            if(map.size() == set.size()) {
                if(right - left < min) {
                    min = right - left;
                    answer[0] = left + 1;
                    answer[1] = right;
                }

            }
        }
        return answer;
    }
}
public class P_보석쇼핑 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.solution(new String[]{"AA", "AB", "AC", "AA", "AC"})));
    }
}

