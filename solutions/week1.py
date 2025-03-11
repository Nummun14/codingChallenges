
# 🕺 אתגר ערבוב רחבת הריקודים! 💃
# במסיבה, אנשים יוצרים שורה של ריקודים. אבל רגע… המארגן רוצה טוויסט! 🔄 הוא רוצה לוודא שאף שני אנשים שהיו צמודים במקור לא יישארו צמודים אחרי הערבוב.
# 🎯 המשימה:
#  כתבו פונקציה dance_shuffle(names) שמקבלת רשימה של שמות ומחזירה רשימה מעורבבת, כך שאף שני אנשים שהיו צמודים במקור לא יהיו צמודים שוב.
# 📌 חוקים מיוחדים:
#  ❌ אם יש שמות כפולים, החזירו "No Duplicates".
#  🚫 אם ערבוב כזה לא אפשרי, החזירו "Cannot shuffle".
#  🎲 בונוס: נסו לערבב כך שאף אחד לא יישאר באותו מקום שבו היה בהתחלה!
# 📍 דוגמאות: בתמונה המצורפת יש דוגמאות למה שהפונקציה יכולה להחזיר אחרי קלטים שונים. ממליץ לבדוק את הפיטרון שלכם איתם.
# `📢 חשוב לציין: לרוב קלטים יש כמה פלטים נכונים. כל עוד הם עומדים בקריטריונים הם תקפים!
#  פתרתם? שתפו את הקוד שלכם כאן! 💬💡
# אז יאללה! תוציאו מחשב, ותתחילו לפתור. בהצלחה!


def dance_shuffle(members):
    length = len(members)
    if length < 4:
        return "Cannot shuffle"
    if len(set(members)) != length:
        return "No duplicates"
    h1 = []
    h2 = []
    for i in range(length):
        if i % 2 == 0:
            h1.append(members[i])
            continue
        h2.append(members[i])
    shuffle = h2 + h1
    if length % 2 != 0:
        shuffle.remove(h1[-1])
        shuffle.insert(length // 2 + 1, h1[-1])
    return shuffle


dance_shuffle(["Nahum", "Yonatan", "Hana", "Noam"])
# יכול להחזיר: ['Yonatan', 'Noam', 'Nahum', 'Hana']
dance_shuffle(["Sarah", "John", "Dana"])
#  יחזיר: Cannot shuffle
dance_shuffle(["Tamir", "Sophie", "Eden", "Tamir"])
# יחזיר: No duplicates
dance_shuffle(["Ron", "James", "Jasmine", "Elisha", "Leah", "Jacob", "Dorit"])
# יכול להחזיר: ['James', 'Elisha', 'Jacob', 'Ron', 'Dorit', 'Jasmine', 'Leah']
