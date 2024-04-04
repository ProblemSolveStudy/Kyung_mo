package javaPs;

import java.util.*;

public class P_JadenCase문자열만들기 {
    class Solution {
        public String solution(String s) {
            String answer = "";
            s = s.toLowerCase();
            StringTokenizer st = new StringTokenizer(s, " ", true);
            List<String> str = new ArrayList<>();

            StringBuilder sb =   new StringBuilder();
            while(st.hasMoreTokens()) {
                String word = st.nextToken();

                if(word.equals(" ")) {
                    sb.append(word);
                } else {
                    sb.append(word.substring(0,1).toUpperCase() + word.substring(1));
                }
            }
            return sb.toString();
        }
    }
}
