package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_14888 {
    static int n;
    static int[] nums;
    static int[] arr = new int[4];
    static int MAX = Integer.MIN_VALUE;
    static int MIN = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        nums = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        backTracking(nums[0], 1);

        System.out.println(MAX);
        System.out.println(MIN);
    }

    private static void backTracking(int num, int idx) {
        if (idx == n) {
            MAX = Math.max(MAX, num);
            MIN = Math.min(MIN, num);
            return;
        }
        for (int i = 0; i < 4; i++) {
            if (arr[i] > 0) {

                arr[i]--;

                switch (i) {
                    case 0:
                        backTracking(num + nums[idx], idx + 1);
                        break;
                    case 1:
                        backTracking(num - nums[idx], idx + 1);
                        break;
                    case 2:
                        backTracking(num * nums[idx], idx + 1);
                        break;
                    case 3:
                        backTracking(num / nums[idx], idx + 1);
                        break;
                }

                arr[i]++;
            }
        }
    }
}
