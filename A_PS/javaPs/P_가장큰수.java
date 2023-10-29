package javaPs;

import java.util.*;

public class P_가장큰수 {
    public static void main(String[] args) {
        String[] strArr = new String[]{"2", "6", "10"};
    }
    class Solution {
        public String solution(int[] numbers) {
            String answer = "";

            String[] strArr = new String[numbers.length];

            for(int i=0; i<numbers.length; i++) {
                strArr[i] = String.valueOf(numbers[i]);
            }

            Arrays.sort(strArr, new Comparator<String>() {
                @Override
                public int compare(String o1, String o2) {
                    return (o1 + o2).compareTo(o2 + o1);
                }
            });


            return answer;
        }
    }
}
