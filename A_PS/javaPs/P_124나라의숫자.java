package javaPs;

public class P_124나라의숫자 {

    public static void main(String[] args) {
        solution(3);
    }
    public static String solution(int n) {
        String answer = "";
        String[] arr = {"4", "1", "2"};

        while(n > 0) {
            int remainder = n%3;
            n /= 3;

            if (remainder % 3 == 0) n--;

            answer = arr[remainder] + answer;
        }
        return answer;
    }
}
