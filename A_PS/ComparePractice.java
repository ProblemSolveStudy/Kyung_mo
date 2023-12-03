import java.util.*;
import java.io.*;


public class ComparePractice
{
    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        StringBuilder sb = new StringBuilder();

        for (char c : str.toCharArray()) {
            if (Character.isUpperCase(c)) {
                sb.append(c);
            }
        }

        System.out.println(sb);
    }
}