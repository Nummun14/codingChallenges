package solutions;

public class Week7 {
    public static int calculateMinimumBreaks(int w, int l) {
        if (w < 1 || l < 1)
            return -1;
        return (w * l) - 1;
    }

    public static int calculateMinimumBreaks(double w, double l, double minSize) {
        if (w < minSize || l < minSize || w % minSize != 0 || l % minSize != 0)
            return -1;

        w /= minSize;
        l /= minSize;
        return (int) (w * l) - 1;
    }

    public static void main(String[] args) {
        calculateMinimumBreaks(2, 2); // 3
        calculateMinimumBreaks(1, -1); // -1

        // bonus
        calculateMinimumBreaks(4, 4, 2); // 3
        calculateMinimumBreaks(2, 1.5, 0.5); // 11
        calculateMinimumBreaks(1.5, 2, 0.7); // -1
    }
}