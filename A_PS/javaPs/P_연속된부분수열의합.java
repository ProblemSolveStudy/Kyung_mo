package javaPs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class P_연속된부분수열의합 {
    public static void main(String[] args) {
        int[] sequence = {1, 1, 1, 2, 3, 4, 5};
        int k = 5;

        int[] result = solution(sequence, k);
        System.out.println(Arrays.toString(result));
    }

    public static int[] solution(int[] sequence, int k) {
        List<int[]> answerList = new ArrayList<>();
        int start = 0;
        int end = -1;
        int sum = 0;

        while (true) {
            if (sum < k) {
                end++;
                if (end >= sequence.length) {
                    break;
                }
                sum += sequence[end];
            } else {
                sum -= sequence[start];
                start++;
                if (start >= sequence.length) {
                    break;
                }
            }

            if (sum == k) {
                answerList.add(new int[]{start, end});
            }

        }

        // 정렬
        answerList.sort((a, b) -> {
            int lengthA = a[1] - a[0];
            int lengthB = b[1] - b[0];
            if (lengthA != lengthB) {
                return lengthA - lengthB;
            } else {
                return a[0] - b[0];
            }
        });

        if (answerList.isEmpty()) {
            return new int[]{-1, -1};
        } else {
            return answerList.get(0);
        }
    }
}
