package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_2661 {
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        dfs("");
    }

    static void dfs(String str) {
        if (str.length() == n) {
            System.out.println(str);
            System.exit(0);
        }

        for (int i = 1; i <= 3; i++) {
            if (checkNums(str + i)) {
                dfs(str + i);
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

//    static int start = 1;
//    static int end = 3;
//    static int n;
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        n = Integer.parseInt(br.readLine());
//
//        dfs("");
//    }
//
//    static void dfs(String str) {
//        if (str.length() == n ) {
//            System.out.println(str);
//            System.exit(0);
//            return;
//        }
//
//        for (int i = start; i <= end; i++) {
//            if (checkStr(str + i)) {
//                dfs(str + i);
//            }
//        }
//    }
//
//    static boolean checkStr(String str) {
//        int len = str.length();
//
//        for (int i = 1; i <= len / 2; i++) {
//            String frontStr = str.substring(str.length() - i - i, str.length() - i);
//            String rearStr = str.substring(str.length() - i, str.length());
//            if(frontStr.equals(rearStr)) return false;
//        }
//        return true;
//    }

}
