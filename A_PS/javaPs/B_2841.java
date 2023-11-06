package javaPs;

import java.util.*;
import java.io.*;
public class B_2841 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        Stack<Integer>[] stack = new Stack[7];
        for(int i=1; i<stack.length; i++) {
            stack[i] = new Stack<>();
        }

        int cnt = 0;

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            int line = Integer.parseInt(st.nextToken());
            int fret = Integer.parseInt(st.nextToken());
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
                cnt++;
            }

        }
        System.out.print(cnt);

    }
}