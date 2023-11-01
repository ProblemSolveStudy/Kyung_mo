package javaPs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
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
        int[] answer = {};
        List<int[]> answerList = new ArrayList<>();
        int start = 0;
        int end = -1;
        int sum = 0;

        while (true) {
            if (sum < k) {
                end++;
                if (end >= sequence.length) break;

                sum += sequence[end];
            } else {
                sum -= sequence[start];
                start++;
                if(start>=sequence.length) break;
            }

            if(sum == k)
                answerList.add(new int[]{start,end});
        }
        Collections.sort(answerList, ((a, b) -> {
            int lengthA = a[1] - a[0];
            int lengthB = b[1] - b[0];

            return lengthA - lengthB;
        }));

        answerList.sort((a,b) -> {
            int lengthA = a[1] - a[0];
            int lengthB = b[1] - b[0];

            return lengthA - lengthB;
        });

        return answerList.get(0);
    }
}
