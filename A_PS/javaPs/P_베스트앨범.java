package javaPs;
import java.util.*;

public class P_베스트앨범 {
    public static void main(String[] args) {
        Solution solution = new P_베스트앨범().new Solution();
        solution.solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{500, 600, 150, 800, 2500});
    }
    class Solution {
        // 두개 씩 모아 베스트 앨범으로 출시
        static class Music {
            int idx;
            int cnt;

            public Music(int idx, int cnt) {
                this.idx = idx;
                this.cnt = cnt;
            }
        }

        public List<Integer> solution(String[] genres, int[] plays) {
            List<Integer> answer = new ArrayList<>();
            Map<String, Integer> map = new HashMap<>();

            for(int i=0; i<genres.length; i++) {
                map.put(genres[i], map.getOrDefault(genres[i], 0) + plays[i]);
            }

            List<String> mapToGenres = new ArrayList<>();
            for(String item : map.keySet()) {
                mapToGenres.add(item);
            }

            mapToGenres.sort((o1, o2) -> map.get(o2) - map.get(o1));
            // System.out.print(mapToGenres);

            for(String item : mapToGenres) {
                List<Music> musics = new ArrayList<>();
                for(int i=0; i<genres.length; i++) {
                    if (item.equals(genres[i])) {
                        musics.add(new Music(i, plays[i]));
                    }
                }

                musics.sort((o1, o2) -> {
                    if(o1.cnt == o2.cnt) {
                        return o1.idx - o2.idx;
                    }
                    return o2.cnt - o1.cnt;
                });

                answer.add(musics.get(0).idx);
                if(musics.size() > 1) {
                    answer.add(musics.get(1).idx);
                }
            }

            return answer;
        }
    }
}
