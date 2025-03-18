package solutions;

public class Week3 {
//    🔀 אתגר "ונהפוך הוא"! 🙃
//    שבוע שעבר חגגנו את פורים! 🎭 החג אולי נגמר, אבל רוח החג ממשיכה גם באתגר של היום. אחד המשפטים המוכרים ביותר מפורים הוא "ונהפוך הוא" – וזה בדיוק מה שנעשה הפעם: נהפוך מילים בתוך משפט!
//            🎯 המשימה:
//    כתבו פונקציה reverse(String sentence) שתקבל מחרוזת ותהפוך את כל המילים בה, מבלי לשנות את סדר המשפט.
//            ⚠ שימו לב!
//    סימני הפיסוק (כמו פסיקים ונקודות) צריכים להישאר בדיוק במקום שבו הם היו. ✍
//            🎲 בונוס:
//    נסו לשמור על כללי הכתיבה – כלומר, שכל משפט יתחיל באות גדולה, ושאר האותיות יהיו קטנות.
//            📍 דוגמאות:
//    בתמונה המצורפת תוכלו לראות דוגמאות לפלט שהפונקציה צריכה להחזיר עבור קלטים שונים. מומלץ לבדוק את הפתרון שלכם בעזרתם!
//            📢 פתרתם? שתפו את הקוד שלכם כאן! 💬💡
//    יאללה, תוציאו מחשב ותתחילו להפוך מילים! 🔄🎉

    private static final String PUNCTUATION = "!”#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
    public static String reverse(String sentence) {
        String[] words = sentence.split(" ");
        StringBuilder reversed = new StringBuilder();
        for (String word : words) {
            StringBuilder punctuation = new StringBuilder();
            StringBuilder wordBuilder = new StringBuilder(word);
            while (PUNCTUATION.contains(wordBuilder.subSequence(wordBuilder.length() - 1, wordBuilder.length()))) {
                punctuation.append(wordBuilder.subSequence(wordBuilder.length() - 1, wordBuilder.length()));
                wordBuilder.replace(wordBuilder.length() - 1, wordBuilder.length(), "");
            }
            reversed.append(reverseWord(wordBuilder.toString()));
            reversed.append(punctuation);
            reversed.append(" ");
        }
        return reversed.toString();
    }

    private static String reverseWord(String word) {
        StringBuilder reversed = new StringBuilder();
        int length = word.length();
        for (int i = 0; i < length; i++) {
            String originalLetterInPlace = word.substring(i, i + 1);
            boolean isLowerCase = originalLetterInPlace.toLowerCase().equals(originalLetterInPlace);
            String letter = word.substring(length - i - 1, length - i);
            if (isLowerCase)
                reversed.append(letter.toLowerCase());
            else
                reversed.append(letter.toUpperCase());
        }
        return reversed.toString();
    }

    public static void main(String[] args) {
        reverse("Hello world!");
        // Olleh dlrow!
        reverse("This is a test.");
        // Siht si a tset.
        reverse("Wow!!! This works? Yes, it does.");
        // Wow!!! Siht skrow? Sey, ti seod.
        reverse("THis iS so cOoL!!!");
        // SIht sI os lOoC!!!
    }
}