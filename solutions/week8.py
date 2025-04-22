import string

first_row = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]"]
second_row = ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'"]
third_row = ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"]
rows = [first_row, second_row, third_row]
# 🔒 אתגר הסיסמה הבטוחה! 🦺
# ידעתם ש־"123456" זו עדיין אחת הסיסמאות הכי נפוצות בעולם?
# אנשים נוטים לבחור סיסמאות פשוטות, ולפעמים צריך לעזור להם לבחור אחת באמת טובה.
# ובשביל זה אנחנו כאן. האתגר היום: לבדוק אם סיסמה באמת בטוחה!
#  🎯 המשימה:
# כתבו פונקציה:
#  isPasswordValid(String password)
# שמקבלת סיסמה, ומחזירה true אם היא בטוחה, או false אם לא.
#
# 🤔 מה זה "סיסמה בטוחה"?
# זה תלוי בכם!
# אפשר לבדוק אורך, אותיות גדולות וקטנות, מספרים, תווים מיוחדים, אולי אפילו אם היא דומה לסיסמה ישנה.
# רוצים? תוסיפו גם בדיקות משעשעות. לגמרי מותר.
# 📢 חשוב:
# המטרה כאן היא יצירתיות – תמציאו בדיקות מקוריות, חכמות או מצחיקות.
# 🎲 בונוס: תדפיסו גם למה הסיסמה לא עברה את הבדיקה.
#
# פתרתם? שתפו את הקוד שלכם כאן! 💬💡
# יאללה, תפתחו מחשב, תקלידו את הסיסמא, ותבדקו אם היא שווה משהו. בהצלחה!


def is_valid_password(password):
    if "69" in password:
        print("Grow up")
        return False
    if "14" not in password:
        print("number 14 must be in password")  # 14 is my luck number
        return False
    if len(password) < 14 or len(password) > 100:
        print("Password must be more then 14 characters and less then 100 characters")
        return False
    if password.islower() or password.isupper():
        print("Password must contain both uppercase and lowercase letters")
        return False
    has_numbers = password[-1].isdigit() or password[-2].isdigit()
    has_punctuation = password[-1] in string.punctuation or password[-2] in string.punctuation
    for i in range(len(password) - 2):
        char = password[i]
        if char.isdigit():
            has_numbers = True
            if password[i + 1].isdigit() and password[i + 2].isdigit():
                if abs(int(password[i + 1]) - int(char)) == 1 and abs(int(password[i + 1]) - int(password[i + 2])) == 1:
                    print("Three consecutive digits aren't allowed")
                    return False
        if char in string.punctuation and not has_punctuation:
            has_punctuation = True
        for row in rows:
            if char in row and password[i + 1] in row and password[i + 2] in row:
                if abs(row.index(char) - row.index(password[i + 1])) == 1 and abs(row.index(password[i + 1]) - row.index(password[i + 2])) == 1:
                    print("Three consecutive letters on the keyboard are not allowed")
                    return False
                break
    if not has_numbers or not has_punctuation:
        print("Password must have punctuation and numbers")
        return False
    return True

