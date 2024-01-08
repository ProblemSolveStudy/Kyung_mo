package javaPs;

import java.io.IOException;
import java.io.*;
import java.util.*;

public class B_16437 {
    static int n;
    static ArrayList<Integer>[] nodes;
    static int[] score;
    static char[] animal;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        nodes = new ArrayList[n + 1];
        animal = new char[n + 1];
        score = new int[n + 1];

        for (int i = 0; i < n+1; i++) {
            nodes[i] = new ArrayList<>();
        }

        for (int i = 2; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());

            char nodeAnimal = st.nextToken().charAt(0);
            int amount = Integer.parseInt(st.nextToken());
            int nextNode = Integer.parseInt(st.nextToken());

            animal[i] = nodeAnimal;
            score[i] = amount;
            nodes[nextNode].add(i);
        }

        System.out.println(postOrder(1));

    }
    private static long postOrder(int node) {
        long sum = 0;

        for (int next : nodes[node]) {
            sum += postOrder(next);
        }

        if (animal[node] == 'S') {
            return sum + score[node];
        } else {
            return (sum - score[node] >= 0) ? sum - score[node] : 0;
        }
    }
}
