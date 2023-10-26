package javaPs;

import java.util.*;

public class P_가장큰수 {
    public static void main(String[] args) {
        String[] strArr = new String[]{"2", "6", "10"};

        int result = "10".compareTo("2"); // -1
        System.out.println(result);

        int result2 = "2".compareTo("10"); // 1 (2보다 10이 더 크다는 뜻)
        System.out.println(result2);
        Arrays.sort(strArr, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                int result3 =  (a+b).compareTo(b+a);
                return result3;
            }
        });

        System.out.println(Arrays.toString(strArr));
    }
    class Solution {
        public String solution(int[] numbers) {
            String answer = "";

            String[] strArr = new String[numbers.length];

            for (int i = 0; i < numbers.length; i++) {
                strArr[i] = Integer.toString(numbers[i]);
            }


            System.out.print(Arrays.toString(strArr));

            return answer;
        }
    }
}
