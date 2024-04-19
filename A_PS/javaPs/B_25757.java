package javaPs;

/**
 * 임스가 미니게임을 같이할 사람을 찾고 있습니다.
 *
 * 플레이할 미니게임으로는 윷놀이 Y,
 * 같은 그림 찾기 F,
 * 원카드 O가 있습니다. 각각 2, 3, 4 명이서 플레이하는 게임이며 인원수가 부족하면 게임을 시작할 수 없습니다.
 *
 * 사람들이 임스와 같이 플레이하기를 신청한 횟수 N과 임스가 플레이할 게임의 종류가 주어질 때,
 * 최대 몇 번이나 임스와 함께 게임을 플레이할 수 있는지 구하시오.
 *
 * 임스와 여러 번 미니게임을 플레이하고자 하는 사람이 있으나,
 * 임스는 한 번 같이 플레이한 사람과는 다시 플레이하지 않습니다.
 *
 * 임스와 함께 플레이하고자 하는 사람 중 동명이인은 존재하지 않습니다.
 * 임스와 lms0806은 서로 다른 인물입니다.
 *
 * 입력
 * 첫 번째 줄에는 사람들이 임스와 같이 플레이하기를 신청한 횟수 N과 같이 플레이할 게임의 종류가 주어진다.
 * 1<= N <= 100000
 *
 * 두 번째 줄부터
 * N개의 줄에는 같이 플레이하고자 하는 사람들의 이름이 문자열로 주어진다.
 * 1 <= 문자열 길이 <= 20
 *
 * 사람들의 이름은 숫자 또는 영문 대소문자로 구성되어 있다.
 *
 * 출력
 * 임스가 최대로 몇 번이나 게임을 플레이할 수 있는지 구하시오.
 */

/**
 7 Y
 lms0806
 lms0806
 exponentiale
 lms0806
 jthis
 lms0806
 leo020630
 * 예제 출력 1
 4
 * 예제 입력 2
 12 F
 lms0806
 powergee
 skeep194
 lms0806
 tony9402
 lms0806
 wider93
 lms0806
 mageek2guanaah
 lms0806
 jthis
 lms0806
 * 예제 출력 2
 3
 * 예제 입력 3
 12 O
 lms0806
 mageek2guanaah
 jthis
 lms0806
 exponentiale
 lms0806
 leo020630
 lms0806
 powergee
 lms0806
 skeep194
 lms0806
 * 예제 출력 3
 2
 */


import java.io.*;
import java.util.*;
public class B_25757 {
    private static final int Y = 1;
    private static final int F = 2;
    private static final int O = 3;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Set<String> set = new HashSet<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int person = Integer.parseInt(st.nextToken());
        String type = st.nextToken();

        for (int i = 0; i < person; i++) {
            set.add(br.readLine());
        }

        int result = 0;
        if (type.equals("Y")) {
            result = set.size() / Y;
        } else if (type.equals("F")) {
            result = set.size() / F;
        } else {
            result = set.size() / O;
        }

        System.out.println(result);
    }
}