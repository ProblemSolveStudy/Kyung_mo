package javaPs;

import java.util.Arrays;

public class test {
    public static void main(String[] args) {
//        int[] c = sum(new int[]{10, 17, 18, 63, 76, 90}, new int[] {20,59,65,77,88, 100, 102});
//
//        for (int i = 0; i < c.length; i++) {
//            System.out.print(c[i] + " ");
//        }

        double initialAmount = 1000000; // 100만원
        double interestRate = 2; // 2%
        int months = 12;

        double finalDeposit = calculateDeposit(initialAmount, interestRate, months);
        System.out.printf("12개월 후의 예치금: %.2f원%n", finalDeposit);

    }

    public static int[] sum (int[] a, int[] b) {
        int minLength = Math.min(a.length, b.length);

        int[] c = new int[minLength];

        for (int i = 0; i < minLength; i++) {
            c[i] = a[i] + b[i];
        }

        return c;
    }
    public static double calculateDeposit(double amount, double annualInterestRate, int months) {
        // 연 이자율을 월 이자율로 변환
        double monthlyInterestRate = annualInterestRate / 100 / 12;

        // 최종 예치금 계산
        double finalAmount = amount * Math.pow(1 + monthlyInterestRate, months);

        return finalAmount;
    }
}

