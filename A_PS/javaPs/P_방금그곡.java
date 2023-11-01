package javaPs;
import java.util.*;

public class P_방금그곡 {
    public static void main(String[] args) {
        Solution solution = new P_방금그곡().new Solution();
        solution.solution("ABC", new String[]{"12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"});
    }
    class Solution {
        public String solution(String m, String[] musicinfos) {
            String answer = "";
            int maxPlayTime = -1;
            m = changeMelody(m);
            Map<String, Integer> map = new LinkedHashMap<>();
            for(int i=0; i<musicinfos.length; i++) {

                String[] info = musicinfos[i].split(",");
                String[] start = info[0].split(":");
                String[] end = info[1].split(":");
                String title = info[2];
                String melody = info[3];
                melody = changeMelody(melody);

                int startH = Integer.valueOf(start[0]);
                int startM = Integer.valueOf(start[1]);
                int endH = Integer.valueOf(end[0]);
                int endM = Integer.valueOf(end[1]);

                int startTime = startH*60 + startM;
                int endTime = endH*60 + endM;

                // 14
                int playTime = endTime-startTime;

                // melody 반복 횟수
                int repeatAll = playTime / melody.length();
                int repeatPart = playTime % melody.length();

                String repeatMelody = melody.repeat(repeatAll) + melody.substring(0,repeatPart);



                for(int j=0; j<=repeatMelody.length() - m.length(); j++) {
                    String temp = repeatMelody.substring(j, j+m.length());

                    if(temp.equals(m) && playTime > maxPlayTime) {
                        answer = title;
                        maxPlayTime = playTime;
                    }
                }


            }
            return maxPlayTime != -1 ? answer : "(None)";
        }

        String changeMelody(String oldMelody) {
            oldMelody = oldMelody.replaceAll("C#", "H");
            oldMelody = oldMelody.replaceAll("D#", "I");
            oldMelody = oldMelody.replaceAll("F#", "J");
            oldMelody = oldMelody.replaceAll("G#", "K");
            oldMelody = oldMelody.replaceAll("A#", "L");

            String newMelody = oldMelody;
            return newMelody;
        }
    }
}
