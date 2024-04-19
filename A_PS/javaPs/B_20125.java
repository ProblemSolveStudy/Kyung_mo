package javaPs;

import java.io.*;
import java.util.*;
public class B_20125 {

    /**
     * 머리가 어딘지 먼저 찾는게 우선일 것 같은데
     */
    public static final char BODY = '*';
    public static final char NON_BODY = '_';

    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    public static char[][] graph;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        graph = new char[N + 1][N + 1];

        int headX = 0;
        int headY = 0;
        for (int i = 1; i <= N; i++) {
            String str = br.readLine();
            for (int j = 1; j <= N; j++) {
                graph[i][j] = str.charAt(j - 1);
            }
        }

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (graph[i][j] == BODY && headX == 0 && headY == 0) {
                    headX = i;
                    headY = j;
                    break;
                }
            }
        }

        int heartX = headX+1;
        int heartY = headY;

        int leftArm=0, rightArm=0, body=0, leftLeg=0, rightLeg=0;

        for (int i = heartY; i > -0; i--) {
            if(graph[heartX][i] == BODY) {
                leftArm++;
            }
        }

        for (int i = heartY; i <= N; i++) {
            if (graph[heartX][i] == BODY) {
                rightArm++;
            }
        }

        int bodyEndX;
        int bodyEndY;
        for (int i = heartX; i <= N; i++) {
            if (graph[i][heartY] == BODY) {
                body++;
            }

            if (i+1 == NON_BODY) {
                bodyEndX = i;
            }
        }

        for (int i = heartX + 1; i <= N; i++) {
            if (graph[i][heartY - 1] == BODY) {
                leftLeg++;
            }

            if (graph[i][heartY + 1] == BODY) {
                rightLeg++;
            }
        }

        System.out.println(heartX + " " + heartY);
        System.out.println((leftArm-1) + " " + (rightArm-1) + " " + (body-1) + " " + leftLeg + " " + rightLeg);
    }
}
