package javaPs;

import java.util.LinkedList;
import java.util.Queue;

public class P_숫자변환하기 {
    public static void main(String[] args) {

    }

    class Solution {
        public int solution(int x, int y, int n) {
            int answer = 0;
            int[] visited = new int[1000001];

            Queue<Integer> q = new LinkedList<>();
            q.offer(x);

            while (!q.isEmpty()) {
                x = q.poll();
                if (x==y) return visited[x];

                int[] nextX = {x + n, x * 2, x * 3};
                for (int nx : nextX) {
                    if (0 <= nx && nx <= 1000000 && visited[nx] == 0) {
                        q.offer(nx);
                        visited[nx] = visited[x] + 1;
                    }
                }
            }
            return answer;
        }
    }
}
