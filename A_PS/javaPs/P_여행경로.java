package javaPs;
import java.util.*;
public class P_여행경로 {
    public static void main(String[] args) {
        Solution solution = new P_여행경로().new Solution();
        solution.solution(new String[][]{{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}});
    }
    class Solution {
        static boolean[] visited;
        static Queue<String> q;
        public String[] solution(String[][] tickets) {
            String[] answer;
            visited = new boolean[tickets.length];
            q = new PriorityQueue<>();
            dfs(tickets, "ICN", 0, "ICN");

            answer = q.peek().split(" ");
            return answer;
        }

        void dfs(String[][] tickets, String currentCity, int cnt, String path) {
            if (cnt == tickets.length) {
                q.add(path);
                return;
            }
            for(int i=0; i<tickets.length; i++) {
                if(!visited[i] && currentCity.equals(tickets[i][0])) {
                    visited[i] = true;
                    dfs(tickets, tickets[i][1], cnt+1, path + " " + tickets[i][1]);
                    visited[i] = false;
                }
            }
        }
    }
}
