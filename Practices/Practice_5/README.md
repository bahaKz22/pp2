# Pracitce_5: Python Regular Expressions (RegEx)
## 1. RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.
**Import the re module:**
```bash
import re
```
---
## 2. RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:
**Functions:**

- **Findall 	- Returns a list containing all matches**
```bash
import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
```
Output:  ```['ai', 'ai']```

- **Search 	- Returns a Match object if there is a match anywhere in the string**
```bash
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
```
Output: ```NONE```

- **Split 	- Returns a list where the string has been split at each match**
```bash
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
```
Output: ```['The', 'rain', 'in', 'Spain']```
```bash
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) 
```
Output: ```['The', 'rain in Spain'] ```

- **Sub 	    - Replaces one or many matches with a string**
```bash 
 import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
```
Output: ```The9rain9in9Spain```
```bash
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x) 
```
Output: ```The9rain9in Spain ```

- **Match - Checks if a string starts with a pattern**
```bash
import re

txt = "Hello world"
x = re.match(r"Hello", txt)

if x:
    print("Match found!")
```
Output: ```Match found!```
- **Compile - Compiles a pattern into a regex object, which can be reused multiple times**
```bash
import re

pattern = re.compile(r"\d+")
txt = "123 abc 456"
numbers = pattern.findall(txt)
print(numbers)
```
Output: ```['123', '456']```
---

## 3. RegEx Syntax and Metacharacters (., *, +, ?, ^, $, [], |, (), \ )
1. **. — Dot**
Definition: Matches any single character except a newline (\n)
```bash
import re

txt = "cat, cot, cut"
x = re.findall(r"c.t", txt)
print(x)
```
Output: ```['cat', 'cot', 'cut']```

2. *** — Asterisk**
Definition: Matches 0 or more repetitions of the previous character or group
```bash
txt = "aaab, ab, b"
x = re.findall(r"a*b", txt)
print(x)
```
Output: ```['aaab', 'ab', 'b']```

3. **+ — Plus**
Definition: Matches 1 or more repetitions of the previous character or group
```bash
txt = "aaab, ab, b"
x = re.findall(r"a+b", txt)
print(x)
```
Output: ```['aaab', 'ab']```

4. **? — Question Mark**
Definition: Matches 0 or 1 occurrence of the previous character or group (makes it optional)
```bash
txt = "color, colour"
x = re.findall(r"colou?r", txt)
print(x)
```
Output: ```['color', 'colour']```

5. **^ — Caret**
Definition: Matches the start of a string
```bash
txt = "Hello world"
x = re.findall(r"^Hello", txt)
print(x)
```
Output: ```['Hello']```

6. **$ — Dollar Sign**
Definition: Matches the end of a string
```bash
txt = "Hello world"
x = re.findall(r"world$", txt)
print(x)
```
Output: ```['world']```

7. **[] — Square Brackets**
Definition: Matches any one character inside the brackets
```bash
txt = "cat, bat, rat"
x = re.findall(r"[cbr]at", txt)
print(x)
```
Output: ```['cat', 'bat', 'rat']```

8. **| — Pipe (OR)**
Definition: Acts as OR, matches either pattern
```bash
txt = "cat, dog, bat"
x = re.findall(r"cat|dog", txt)
print(x)
```
Output: ```['cat', 'dog']```

9. **() — Parentheses**
Definition: Groups patterns together and can capture matches
```bash
txt = "red, green, blue"
x = re.findall(r"(re)d", txt)
print(x)
```
Output: ```['re']```

10. **\ — Backslash (Escape)**
Definition: Escapes a metacharacter to match it literally or introduces a special sequence
```bash
txt = "1 + 2 = 3"
x = re.findall(r"\+", txt)
print(x)
```
Output: ```['+']```

---
## 4. Special Sequences (\d, \w, \s, \D, \W, \S, \A, \Z)
1. **\d — Digit**
Definition (EN): Matches any digit (0–9).
Определение (RU): Соответствует любой цифре от 0 до 9.
```bash
import re

txt = "My phone: 12345"
x = re.findall(r"\d", txt)
print(x)
```
Output: ```['1', '2', '3', '4', '5']```

2. **\D — Non-Digit / Не цифра**
Definition (EN): Matches any character that is not a digit.
Определение (RU): Соответствует любому символу, который не является цифрой.
```bash
txt = "My phone: 12345"
x = re.findall(r"\D", txt)
print(x)
```
Output: ```['M', 'y', ' ', 'p', 'h', 'o', 'n', 'e', ':', ' ']```

3. **\w — Word Character / Словесный символ**
Definition (EN): Matches letters, digits, and underscore (a-z, A-Z, 0-9, _).
Определение (RU): Соответствует буквам, цифрам и символу подчеркивания.
```bash
txt = "Hello_123!"
x = re.findall(r"\w", txt)
print(x)
```
Output: ```['H', 'e', 'l', 'l', 'o', '_', '1', '2', '3']```

4. **\W — Non-Word Character / Не словесный символ**
Definition (EN): Matches any character that is not a letter, digit, or underscore.
Определение (RU): Соответствует любому символу, который не буква, не цифра и не _.
```bash
txt = "Hello_123!"
x = re.findall(r"\W", txt)
print(x)
```
Output: ```['!']```

5. **\s — Whitespace / Пробел**
Definition (EN): Matches any whitespace character (space, tab, newline).
Определение (RU): Соответствует любому пробельному символу ( , \t, \n).
```bash
txt = "Hello world"
x = re.findall(r"\s", txt)
print(x)
```
Output: ```[' ']```

6. **\S — Non-Whitespace / Не пробел**
Definition (EN): Matches any character that is not a whitespace.
Определение (RU): Соответствует любому символу, который не является пробельным.
```bash
txt = "Hello world"
x = re.findall(r"\S", txt)
print(x)
```
Output: ```['H','e','l','l','o','w','o','r','l','d']```

7. **\A — Start of String / Начало строки**
Definition (EN): Matches the start of the string.
Определение (RU): Соответствует началу строки.
```bash
txt = "Hello world"
x = re.findall(r"\AHello", txt)
print(x)
```
Output: ```['Hello']```

8. **\Z — End of String / Конец строки**
Definition (EN): Matches the end of the string.
Определение (RU): Соответствует концу строки.
```bash
txt = "Hello world"
x = re.findall(r"world\Z", txt)
print(x)
```
Output: ```['world']```

---
## 5. Sets and Character Classes
1. **Sets / Наборы [ ]**
Definition (EN): A set defines a group of characters. Matches any single character inside the brackets.
Определение (RU): Набор [ ] определяет группу символов. Соответствует любому одному символу из набора.
```bash
import re

txt = "cat, bat, rat, mat"
x = re.findall(r"[cbr]at", txt)
print(x)
```
Output: ```['cat', 'bat', 'rat']```

2. **Ranges / Диапазоны -**
Definition (EN): Matches any character within a range.
Определение (RU): Соответствует любому символу в указанном диапазоне.
```bash
txt = "a1 b2 c3 d4"
x = re.findall(r"[a-c][1-3]", txt)
print(x)
```
Output: ```['a1', 'b2', 'c3']```

3. **Negation / Отрицание [^ ]**
Definition (EN): Matches any character NOT in the set.
Определение (RU): Соответствует любому символу, которого нет в наборе.
```bash
txt = "cat, bat, rat"
x = re.findall(r"[^bcr]at", txt)
print(x)
```
Output: ```[]```

4. **Predefined Character Classes / Предопределённые классы**
![ex](https://github.com/bahaKz22/pp2/blob/main/Practices/Practice_5/Screenshot_06-Mar_22-29-38.png)

```bash
txt = "Hello 123!"
x = re.findall(r"[\w\s]", txt)
print(x)
```
Output: ```['H','e','l','l','o',' ','1','2','3']```

5. **Combination / Комбинации**
Можно комбинировать диапазоны и классы:
```bash
txt = "a1 B2 c3 #$%"
x = re.findall(r"[a-zA-Z0-9]", txt)
print(x)
```
Output: ```['a', '1', 'B', '2', 'c', '3']```

---
## 6. Quantifiers ({n}, {n,}, {n,m})
1. **{n} — Exact Number / Точное количество**
Definition (EN): Matches exactly n repetitions of the previous character or group.
Определение (RU): Соответствует ровно n повторениям предыдущего символа или группы.
```bash
import re

txt = "aa aaaa aaa"
x = re.findall(r"a{3}", txt)
print(x)
```
Output: ```['aaa', 'aaa']```

2. **{n,} — At Least / Минимум n**
Definition (EN): Matches at least n repetitions of the previous character or group.
Определение (RU): Соответствует минимум n повторениям предыдущего символа или группы.
```bash
txt = "aa aaaa aaa a"
x = re.findall(r"a{2,}", txt)
print(x)
```
Output: ```['aa', 'aaaa', 'aaa']```

3. **{n,m} — Range / Диапазон n до m**
Definition (EN): Matches between n and m repetitions of the previous character or group.
Определение (RU): Соответствует от n до m повторений предыдущего символа или группы.
```bash
txt = "a aaaa aaa aa"
x = re.findall(r"a{2,3}", txt)
print(x)
```
Output: ```['aaa', 'aa', 'aa']```

---
## 7. Flags (re.IGNORECASE, re.MULTILINE, etc.)
1. **re.IGNORECASE / re.I — Ignore Case**
Definition (EN): Makes the pattern case-insensitive.
Определение (RU): Игнорирует регистр символов при поиске.
```bash
import re

txt = "Hello hello HeLLo"
x = re.findall(r"hello", txt, re.IGNORECASE)
print(x)
```
Output: ```['Hello', 'hello', 'HeLLo']```

2. **re.MULTILINE / re.M — Multiline**
Definition (EN): Changes ^ and $ to match start and end of each line, not just the whole string.
Определение (RU): Символы ^ и $ соответствуют началу и концу каждой строки, а не только всей строки.
```bash
txt = "Hello\nWorld"
x = re.findall(r"^World", txt, re.MULTILINE)
print(x)
```
Output: ```['World']```

3. **re.DOTALL / re.S — Dot Matches All**
Definition (EN): Makes . match any character including newline.
Определение (RU): Символ . соответствует любому символу, включая перенос строки.
```bash
txt = "Hello\nWorld"
x = re.findall(r"Hello.*World", txt, re.DOTALL)
print(x)
```
Output: ```['Hello\nWorld']```

4. **re.VERBOSE / re.X — Verbose / Readable**
Definition (EN): Allows comments and whitespace in the pattern for readability.
Определение (RU): Позволяет писать комментарии и пробелы в шаблоне для удобного чтения.
```bash
txt = "123-456-7890"
pattern = re.compile(r"""
    \d{3}  # area code
    -      # dash
    \d{3}  # first 3 digits
    -      # dash
    \d{4}  # last 4 digits
""", re.VERBOSE)

x = pattern.findall(txt)
print(x)
```
Output: ```['123-456-7890']```

5. **Common Flags / Часто используемые флаги**
![flags](https://github.com/bahaKz22/pp2/blob/main/Practices/Practice_5/Screenshot_06-Mar_23-05-03.png)
