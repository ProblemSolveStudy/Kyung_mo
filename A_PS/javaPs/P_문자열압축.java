package javaPs;

import java.util.*;
public class P_문자열압축 {
    public static void main(String[] args) {

    }
    class Solution {
        public int solution(String s) {
            int answer = s.length();

            if(s.length() == 1) return 1;

            for(int i=1; i<=s.length()/2; i++) {
                StringBuilder sb = new StringBuilder();
                String temp = "";
                int cnt = 1;

                for(int j=0; j<s.length(); j+= i) {
                    String repeatChar = s.substring(j,j+1);

                    if(repeatChar.equals(temp)) {
                        cnt++;
                        continue;
                    } else if (cnt > 1) {
                        sb.append(cnt+temp);
                        cnt = 1;
                    } else {
                        sb.append(repeatChar);
                    }
                    temp = repeatChar;
                }
                sb.append(cnt > 1 ? cnt + temp : temp);

                if (s.length() % i != 0) {
                    sb.append(s.substring(s.length() - s.length() % i, s.length()));
                }

                answer = Math.min(answer, sb.length());
            }
            return answer;
        }
    }
}
