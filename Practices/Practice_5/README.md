# Pracitce_5: Python Regular Expressions (RegEx)
## 1.RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.
**Import the re module:**
```bash
import re
```
---
## 2.RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:
- **Function 	- Description:**

- **findall 	- Returns a list containing all matches**
```bash
import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
```
Output:  ```bash['ai', 'ai']```

- **search 	- Returns a Match object if there is a match anywhere in the string**
```bash
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
```
Output: ```bashNONE```

- **split 	- Returns a list where the string has been split at each match**
```bash
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
```
Output: ```bash  ['The', 'rain', 'in', 'Spain']```
```bash
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) 
```
Output: ```bash  ['The', 'rain in Spain'] ```

- **sub 	    - Replaces one or many matches with a string**
```bash 
 import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
```
Output: ```bash  The9rain9in9Spain```
```bash
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x) 
```
Output: ```bash  The9rain9in Spain ```
---

