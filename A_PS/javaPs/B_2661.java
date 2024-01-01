package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B_2661 {
    static int n;
    static String temp = "";

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        backTracking("");
    }

    static void backTracking(String str) {
        if (str.length() == n) {
            System.out.println(str);
            System.exit(0);
        }
        for (int i = 1; i <= 3; i++) {
            if (checkNums(str + i)) {
                backTracking(str + i);
            }
        }
    }

    static boolean checkNums(String str) {
        for (int i = 1; i <= str.length() / 2; i++) {
            String rear = str.substring(str.length() - i, str.length());
            String front = str.substring(str.length() - i - i, str.length() - i);

            if(rear.equals(front)) return false;
        }
        return true;
    }
}
