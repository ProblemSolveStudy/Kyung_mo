package javaPs;

public class P_2개이하로다른비트 {
    class Solution {
        public long[] solution(long[] numbers) {
            long[] answer = new long[numbers.length];

            for (int i=0; i<numbers.length; i++) {
                long targetNum = numbers[i];

                if (targetNum % 2 == 0) {
                    answer[i] = targetNum + 1;
                } else {
                    String s = Long.toString(numbers[i], 2); // 2진수로 변경
                    int zeroIdx = s.lastIndexOf("0");

                    if (zeroIdx == -1) {
                        s = "10" + s.substring(1, s.length());
                        answer[i] = Long.parseLong(s, 2);
                    } else {
                        s = s.substring(0,zeroIdx) + "10" + s.substring(zeroIdx+2, s.length());
                        answer[i] = Long.parseLong(s, 2);
                    }
                }
            }

            return answer;
        }


    }

    public static void main(String[] args) {
        Solution solution = new P_2개이하로다른비트().new Solution();
        solution.solution(new long[]{2,9});
    }
}
