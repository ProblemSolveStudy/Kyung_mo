package javaPs;
import java.util.*;
public class P_타겟넘버 {
    public static void main(String[] args) {

    }

    class Solution {
        static int count = 0;
        public int solution(int[] numbers, int target) {
            int answer = 0;
            dfs(numbers, 0, target, 0);
            return count;
        }

        public void dfs(int[] numbers, int depth, int target, int result) {
            if(depth == numbers.length) {
                if (target == result) {
                    count++;
                }
                return;
            }

            int plus = result + numbers[depth];
            int minus = result - numbers[depth];

            dfs(numbers, depth+1, target, plus);
            dfs(numbers, depth+1, target, minus);
        }
    }
}
