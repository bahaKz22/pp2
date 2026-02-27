from datetime import datetime
now = datetime.now()

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
'''
| Code | Meaning      |
| ---- | ------------ |
| %Y   | 4-digit year |
| %y   | 2-digit year |
| %m   | month        |
| %d   | day          |
| %H   | hour (24h)   |
| %I   | hour (12h)   |
| %M   | minute       |
| %S   | second       |
| %A   | weekday name |
| %B   | month name   |

'''