import java.util.Arrays;
import java.util.Comparator;

public class ComparePractice {
    public static void main(String[] args) {
        int[][] arrays = { { 0, 3 }, { 2, 6 }, { 1, 9 }, { 1, 8 } };

        Arrays.sort(arrays, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) return  o2[1]-o1[1];
                else return o2[0]-o1[0];
            }
        });

        System.out.println(Arrays.deepToString(arrays));
    }
}
