package javaPs;

import java.util.*;
public class P_디스크컨트롤러 {
    public static void main(String[] args) {

    }
    class Solution {
        public int solution(int[][] jobs) {
            int answer = 0;

            Arrays.sort(jobs, (o1, o2)-> o1[1] - o1[0] - (o2[1] - o2[0]));

            

            return answer;
        }
    }
}
