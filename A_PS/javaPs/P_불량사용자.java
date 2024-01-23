package javaPs;

import java.util.*;
public class P_불량사용자 {
    public static void main(String[] args) {
        Solution solution = new P_불량사용자().new Solution();

        System.out.println(solution.solution(new String[]{"frodo", "fradi", "crodo", "abc123", "frodoc"}, new String[]{"fr*d*", "abc1**"}));

    }


    class Solution {
        static HashSet<HashSet<String>> result = new HashSet<>();
        public int solution(String[] user_id, String[] banned_id) {
            int answer = 0;
            dfs(new HashSet<String>(), 0, user_id, banned_id);

            return result.size();
        }

        private static void dfs(HashSet<String> set, int depth, String[] user_id, String[] banned_id) {
            if (depth == banned_id.length) {
                result.add(set);
                return;
            }

            for(int i=0; i<user_id.length; i++) {
                if (set.contains(user_id[i])) {
                    continue;
                }
                if(check(user_id[i], banned_id[depth])) {
                    set.add(user_id[i]);
                    dfs(new HashSet<>(set), depth+1, user_id, banned_id);
                    set.remove(user_id[i]);
                }
            }
        }

        private static boolean check(String userId, String bannedId) {
            if (userId.length() != bannedId.length()) return false;

            for(int i=0; i<userId.length(); i++) {
                if(bannedId.charAt(i) != '*' && userId.charAt(i) != bannedId.charAt(i)) {
                    return false;
                }
            }

            return true;
        }
    }
}
