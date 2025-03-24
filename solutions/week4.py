import math


# 🔢 אתגר העצרת ההפוך!📐
# לפני שבועיים היה פה שיח לגביי האם יש לעצרת פעולה הפוכה. כשראיתי את זה הסתקרנתי, והתחלתי לחשוב. וזה דווקא לא כזה מסובך. אז זה האתגר של היום: להכין פעולה הפוכה לעצרת!
# 🎯 המשימה:
# כתבו פונקציה בשם reverseFactorial(int num) שתקבל מספר שעבר עצרת, ותחזיר את המספר המקורי.
# 📌חוקים מיוחדים
# ⛔ אם אין למספר עצרת הפוך, הפונקציה תחזיר -1.
# ⚠ שימו לב!
#  יש כמה דרכים לפתור את זה, אז גם אם פתרתם, תנסו לחשוב על פתרון יעיל יותר.
# 📍 דוגמאות:
# בתמונה המצורפת תוכלו לראות דוגמאות לפלט שהפונקציה צריכה להחזיר עבור קלטים שונים. מומלץ לבדוק את הפתרון שלכם בעזרתן!
# 📢 פתרתם? שתפו את הקוד שלכם כאן ! 💬💡
#  יאללה, תוציאו מחשב, תפתחו את ה-IDE, ותתחילו לפתור!🔥🏅


def reversed_factorial(factorial):
    num = 1
    while math.factorial(num) < factorial:
        num += 1

    if math.factorial(num) == factorial:
        return num
    return -1


def most_efficient_reversed_factorial(factorial):
    num = 1
    while factorial % num == 0:
        factorial //= num
        num += 1

    return num - 1 if factorial == 1 else -1


reversed_factorial(120)
# יחזיר 5
reversed_factorial(24)
# יחזיר 4
reversed_factorial(150)
# יחזיר -1
reversed_factorial(1)
# יחזיר 1
