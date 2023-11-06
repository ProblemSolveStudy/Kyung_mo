package javaPs;

public class P_숫자카드나누기 {
    class Solution {
        public int solution(int[] arrayA, int[] arrayB) {
            int answer = 0;
            int gcdA = arrayA[0];
            int gcdB = arrayB[0];

            for(int i=1; i<arrayA.length; i++) {
                gcdA = gcd(arrayA[i], gcdA);
            }
            for(int i=1; i<arrayB.length; i++) {
                gcdB = gcd(arrayB[i], gcdB);
            }

            if (notDiv(arrayA, gcdB)) answer = Math.max(answer, gcdB);
            if (notDiv(arrayB, gcdA)) answer = Math.max(answer, gcdA);

            return answer;
        }

        public int gcd(int a, int b) {
            if (a % b == 0) return b;
            return gcd(b, a%b);
        }

        public boolean notDiv(int[] array, int gcdNum) {
            for(int num : array) {
                if (num % gcdNum == 0) return false;
            }
            return true;
        }


    }
}
