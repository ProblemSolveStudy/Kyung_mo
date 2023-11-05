package javaPs;
import java.util.*;
import java.io.*;
public class B_2792 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 항상 같은 색의 보석만을 가진다.
        String s = br.readLine();
        int answer =0 ;

        int n = Integer.parseInt(s.split(" ")[0]);
        int m = Integer.parseInt(s.split(" ")[1]);

        List<Integer> list = new ArrayList<>();
        for(int i=0; i<m; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(list);

        int start = 1;
        int end = list.get(list.size()-1);

        while (start <= end) {
            int mid = (start + end) / 2;
            int sum =0;
            for (int i = 0; i < m; i++) {
                sum += list.get(i) / mid;
                if (list.get(i) % mid != 0) {
                    sum++;
                }
            }

            if (sum > n) start = mid + 1;
            else {
                end = mid - 1;
                answer = mid;
            }
        }
        System.out.println(answer);
    }
}
