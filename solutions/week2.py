import math
import string
import week1

# *🔒אתגר הצפנת סיסמאות!🗝️*
# בלי הצפנה, סיסמאות לא בטוחות – ולכן אנחנו צריכים הצפנה! כיום קיימות המון שיטות הצפנה, אבל רובן… איך לומר? *לא כיפיות*. האתגר שלנו: *ליצור הצפנה מקורית ומהנה!*
# *🎯המשימה:*
# כתבו פונקציה ```encrypt(password)``` שתקבל סיסמא, ותחזיר אותה מוצפנת, כך שאי אפשר לדעת מה הסיסמא הייתה במקור.
# *⚠️שימו לב!:* לכל סיסמה צריך להיות גרסה מוצפנת _אחת_  בלבד.
# *🎲בונוס:* צרו הצפנה שגם אם יודעים את השיטה שלכם – אי אפשר לשחזר את הסיסמה המקורית. (רמז: יש פעולות מתמטיות שאין להן פעולה הפוכה 😉).
# *📢חשוב לציין:* אל תשתמשו בספריות הצפנה מוכנות! תכננו שיטה מקורית משלכם.
# פתרתם? שתפו את הקוד שלכם כאן! 💬💡
# אז יאללה! תוציאו מחשב, תקלידו את הסיסמה, ותתחילו להצפין אותה. בהצלחה!


def encrypt(password):
    printable = string.printable
    shuffle = week1.dance_shuffle(password)
    str_shuffle = "".join(shuffle)
    shuffle = ""

    for i in range(len(password)):
        shuffle += printable[(printable.index(password[i]) + i) % len(printable)]
        if i < len(str_shuffle):
            shuffle += printable[(printable.index(str_shuffle[i]) + i) % len(printable)]
        shuffle += str((printable.index(password[i])) ** 2)
        if shuffle[-1] in string.digits:
            shuffle += str(math.factorial(int(shuffle[-1])))

    return shuffle.replace(" ", "").replace("\n", "").replace("\r", "")


encrypt("qwerty")
# qw676720xs102424gA196720ut729362880xi8411Dy1156720
encrypt("password123")
# pN625120bp1001u78424vg78424Ay102424tu576720xr729362880kp1693628809k11bj424dD9362880
encrypt("veryGoodAndStrongPassword")
# vN9611fp196720t729362880Bg1156720Ky176424tu576720ur576720kp169362880Ik1296720wj529362880nD169362880$p2916720FE8411E729362880C576720C529362880w256720'26011s1001L78424M78424R102424K576720O729362880B169362880
