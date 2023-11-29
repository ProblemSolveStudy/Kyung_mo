package javaPs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class B_2798 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int target = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Integer[] nums = new Integer[n];
        for(int i=0; i<n; i++) {
            nums[i] = Integer.valueOf(st.nextToken());
        }
        int result = Integer.MIN_VALUE;
        int temp = 0;

        for(int i=0; i<n; i++) {
            for(int j=i+1; j<n; j++) {
                for(int k=j+1; k<n; k++) {
                    result = nums[i] + nums[j] + nums[k];

                    temp = (temp < result && result <= target) ? result : temp;
                }
            }
        }
        System.out.println(temp);

    }
}
