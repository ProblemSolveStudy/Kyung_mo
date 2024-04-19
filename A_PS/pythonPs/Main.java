package pythonPs;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        dept();
        user();
    }

    public static void dept() {
        String originalData = "나|C300220620|1234|신한|Shinhan Bank||AIsp|신한은행(홍훙ㅎ웋ㅇ)|1|3|C300220619|SH|SH|TOP|SH||||||";
        String[] parts = originalData.split("\\|");
        int numberToIncrement = Integer.parseInt(parts[2]);

        List<String> newDataList = new ArrayList<>();

        for (int i = 0; i < 15000; i++) {
            // 3번째 요소를 1씩 증가시키며 새로운 데이터 생성
            parts[2] = String.valueOf(numberToIncrement + i);
            String newData = String.join("|", parts) + "||||||";
            newDataList.add(newData);
        }

        // 새로운 데이터를 텍스트 파일에 저장
        String fileName = "SG_ORG_DEPT_20240415.txt";
        try (FileWriter writer = new FileWriter(fileName)) {
            for (String newData : newDataList) {
                writer.write(newData + System.lineSeparator());
            }
            System.out.println("새로운 데이터가 " + fileName + "에 저장되었습니다.");
        } catch (IOException e) {
            System.err.println("파일 저장 중 오류가 발생했습니다: " + e.getMessage());
        }
    }

    private static void user() {
        String originalData = "SH|2313|인텔|SUNG HO KANG|수석|31036|수석|호본부|D646347408|신한은행|sh06162576@swingdev.shinhan.com|4급|1|ksh2002@shinhan.com|2|19730|01000000001|5-8419|02-2151-8419|0505-178-0172|1234|SH068|h|N|N|SH|||||";
        String[] parts = originalData.split("\\|");
        int numberToIncrement = Integer.parseInt(parts[1]);
        int numberToDept = Integer.parseInt(parts[20]);

        List<String> newDataList = new ArrayList<>();

        for (int i = 0; i < 15000; i++) {
            // 배열을 복제하여 새로운 배열 생성
            String[] newParts = Arrays.copyOf(parts, parts.length);
            // 새로운 배열의 요소를 수정
            newParts[1] = String.valueOf(numberToIncrement + i);
            newParts[20] = String.valueOf(numberToDept + i);
            String newData = String.join("|", newParts) + "|||||";
            newDataList.add(newData);
        }

        // 새로운 데이터를 텍스트 파일에 저장
        String fileName = "SG_ORG_USER_20240415.txt";
        try (FileWriter writer = new FileWriter(fileName)) {
            for (String newData : newDataList) {
                writer.write(newData + System.lineSeparator());
            }
            System.out.println("새로운 데이터가 " + fileName + "에 저장되었습니다.");
        } catch (IOException e) {
            System.err.println("파일 저장 중 오류가 발생했습니다: " + e.getMessage());
        }
    }

}
