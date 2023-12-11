import java.util.*;
import java.io.*;


public class ComparePractice
{
    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String temp = br.readLine();

        for (int i = 0; i < temp.length(); i++) {
            System.out.println(temp.charAt(i) - 'A');
        }

    }
}