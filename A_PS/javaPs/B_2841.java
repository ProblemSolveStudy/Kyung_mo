package javaPs;

import java.util.*;
import java.io.*;
public class B_2841 {
    public static void main(String[] args) throws IOException {
        // 기타 6줄
        // 각 줄은 1번부터 P번까지의 프랫으로 이뤄져 있음
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        //음의 수 N
        int n = Integer.parseInt(s.split(" ")[0]);
        int p = Integer.parseInt(s.split(" ")[1]);
        Stack<Integer>[] stack = new Stack[7];

        for(int i=1; i<7; i++) {
            stack[i] = new Stack<>();
        }
        int cnt = 0;

        for(int i=0; i<n; i++) {
            s = br.readLine();
            int line = Integer.parseInt(s.split(" ")[0]);
            int fret = Integer.parseInt(s.split(" ")[1]);

            while (!stack[line].isEmpty()) {
                if (stack[line].peek() < fret) {
                    stack[line].push(fret);
                } else if (stack[line].peek() > fret) {
                    stack[line].pop();
                } else {
                    break;
                }
                cnt++;
            }

            if (stack[line].isEmpty()) {
                stack[line].push(fret);
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}
