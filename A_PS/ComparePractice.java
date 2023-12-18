import java.util.*;
import java.io.*;


public class ComparePractice
{
    public static void main(String args[]) throws IOException
    {
        ArrayList<Integer> list = new ArrayList<>();
        int n = 1;
        while (n <= 200) {
            if (n % 3 == 0 && n % 7 != 0) {
                list.add(n);
            }

            n++;
        }

        int cnt = 0;
        for (int i : list) {
            cnt += i;
        }
        System.out.println(cnt);
        System.out.println(list.size());
    }

}