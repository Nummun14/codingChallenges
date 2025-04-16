package solutions;

public class Week7 {
    public static int calculateMinimumBreaks(double width, double length) {
        if (width < 1 || length < 1)
            return -1;
        return (width * length) - 1;
    }

    public static int calculateMinimumBreaks(double width, double length, double squareSize) {
        if (width < squareSize || length < squareSize || width % squareSize != 0 || length % squareSize != 0)
            return -1;

        width /= squareSize;
        length /= squareSize;
        return (int) (width * length) - 1;
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