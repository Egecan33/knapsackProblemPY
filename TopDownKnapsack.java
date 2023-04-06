import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TopDownKnapsack {

    public static List<Integer> topDown(int i, int[] v, int[] w, int size) {
        int takeValue = 0;
        int doNotTakeValue = 0;
        List<Integer> take = new ArrayList<>();
        List<Integer> doNotTake = new ArrayList<>();

        if (i == 0) {
            return new ArrayList<>();
        }

        if (i >= 1) {
            if (w[i - 1] <= size) {
                take = topDown(i - 1, v, w, size - w[i - 1]);
                takeValue = v[i - 1];
                for (int value : take) {
                    takeValue += value;
                }
            }
            doNotTake = topDown(i - 1, v, w, size);

            for (int value : doNotTake) {
                doNotTakeValue += value;
            }

            if (takeValue > doNotTakeValue) {
                take.add(v[i - 1]);
                return take;
            } else {
                return doNotTake;
            }
        }

        return new ArrayList<>();
    }

    public static void main(String[] args) {
        int[] values = { 65, 100, 120, 230 };
        int[] weights = { 10, 20, 30, 45 };
        int size = 50;
        int n = values.length;
        // enter the values and weights in the array

        Map<Integer, Integer> valueIndexMap = new HashMap<>();
        for (int i = 0; i < values.length; i++) {
            valueIndexMap.put(values[i], i);
        }

        List<Integer> selectedItems = topDown(n, values, weights, size);
        int maxValue = 0;
        for (int value : selectedItems) {
            maxValue += value;
            System.out.println("Selected item index: " + valueIndexMap.get(value));
        }
        System.out.println("Maximum value: " + maxValue);
    }
}
