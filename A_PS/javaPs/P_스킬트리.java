package javaPs;

import java.util.*;
public class P_스킬트리 {
    public static void main(String[] args) {
        Solution solution = new P_스킬트리().new Solution();
        solution.solution("CBD", new String[]{"BACDE", "CBADF", "AECB", "BDA"});
    }
    class Solution {
        public int solution(String skill, String[] skill_trees) {
            int answer = 0;

            List<Character> skillArr = new ArrayList<>();
            for (int i=0; i<skill.length(); i++) {
                skillArr.add(skill.charAt(i));
            }

            for (String skills : skill_trees) {
                boolean[] visited = new boolean[skillArr.size()];
                boolean isPossible = true;

                for (int i = 0; i < skills.length(); i++) {
                    if (skillArr.contains(skills.charAt(i))) {

                        // B의 위치에 true로 만들어 줘야 함
                        int skillArrIdx = skillArr.indexOf(skills.charAt(i));

                        if (skillArrIdx == 0) {
                            visited[skillArrIdx] = true;
                        }
                        // 근데 B의 앞 visited가 false면?
                        else {
                            if (visited[skillArrIdx - 1] == false) {
                                isPossible = false;
                                break;
                            }
                            visited[skillArrIdx] = true;
                        }
                    }
                }
                if (isPossible) {
                    answer++;
                }
            }
            return answer;
        }
    }

}
