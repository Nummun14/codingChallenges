package solutions;

public class Week7 {
//    🥖אתגר חלוקת המצה! 🍞
//    חג שמח לכולם!
//    באתגר של היום אנחנו שוברים את הראש. או יותר נכון, את המצה!
//    המטרה: לחלק את המצה לריבועים שווים, בלי להשאיר שאריות, ובכמה שפחות שבירות!
//            🎯 המשימה:
//    כתבו פונקציה
//    calculateMinBreaks(double width, double length)
//    שמקבלת אורך ורוחב של מצה, ומחזירה את הכמות שבירות המינימלית כדי לחלק את המצה לריבועים שווים שכל צלע באורך של 1 ס''מ, בלי שארית.
//            ⚠ חוקים מיוחדים:
//            🙌 חייבים לחלק את המצה בצורה מדויקת. בלי שאריות .
//            ⿡ כל ריבוע צריך להיות בדיוק בגודל של 1 ס"מ על 1 ס"מ.
//❌ אם אי אפשר לחלק את המצה בלי שארית, הפונקציה תחזיר -1.
//            🎲בונוס: תוסיפו פרמטר double squareSize ותתאימו את הפונקציה כך שהיא תעבוד לכל גודל ריבוע.
//🍭 דוגמאות:
//    בתמונה המצורפת תוכלו לראות דוגמאות לפלט שהפונקציה צריכה להחזיר עבור קלטים שונים. מומלץ לבדוק את הפתרון שלכם בעזרתם!
//            📢 פתרתם? שתפו את הקוד שלכם כאן! 💬💡
//            יאללה, תוציאו מצה – ותתחילו לשבור!
//    בהצלחה!

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