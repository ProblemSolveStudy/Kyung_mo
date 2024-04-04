package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_5073 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            // 가장 길이가 긴 변을 max 로 지정한다.
            // 세 변의 길이가 삼각형의 조건을 만족하지 못하면 Invalid
            // a^2 + b^2 = c^2
            // 세 변의 길이가 같으면 Equilateral
            // 두 변의 길이만 같으면 Isosceles
            // 세 변의 길이가 모두 다르면 Scalene

            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 0 && b == 0 && c == 0) {
                break;
            }
            if (isTriangle(a, b, c)) {
                check(a, b, c);
            } else {
                System.out.println("Invalid");
            }
        }
    }

    public static boolean isTriangle(int a, int b, int c) {
        boolean b3 = b + c > a;
        boolean b2 = a + c > b;
        boolean b1 = a + b > c;

        if (b1 && b2 && b3) return true;
        else return false;
    }

    public static void check(int a, int b, int c) {
        if (a != b && b != c && a != c) {
            System.out.println("Scalene");
        } else if (a == b && b == c) {
            System.out.println("Equilateral");
        } else {
            System.out.println("Isosceles");

        }
    }

}
