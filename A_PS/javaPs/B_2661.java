package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B_2661 {
    static int n;
    static String result = "";
    static final int START = 1;
    static final int END = 3;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        /**
         * 1,2,3 으로 이뤄진 수열을 하나씩 찾아가며 중복되는지 안되는지 알아내야 한다.
         * 그렇기 때문에 백트래킹을 활용하도록 하자
         */

        dfs("");
    }

    static void dfs(String str) {
        if (str.length() == n) {
            System.out.println(str);
            System.exit(0);
        }

        for (int i = START; i <= END; i++) {
            if(checkNum(str + i)) {
                dfs(str + i);
            }
        }
    }

    static boolean checkNum(String str) {
        for (int i = 1; i <= str.length()/2; i++) {
            String front = str.substring(str.length() - i - i, str.length() - i);
            String rear = str.substring(str.length() - i, str.length());

            if (front.equals(rear)) {
                return false;
            }
        }
        return true;
    }
}
