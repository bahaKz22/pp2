'''
\r	Carriage Return
\t	Tab
\b	Backspace
\f	Form Feed
\ooo	Octal value
\xhh	Hex value
'''
txt = "Hello\bWorld!"
print(txt)
# Output: HellWorld!
txt = "Hello\fWorld!"
print(txt)
# Output: Hello
#         World!
txt = "Hello\rWorld!"
print(txt)
# Output: World!lo
txt = "Hello\tWorld!"
print(txt)
# Output: Hello   World!
txt = "\110\145\154\154\157"
print(txt)
# Output: Hello
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
# Output: Hello
txt = "Hello\\World!"
print(txt)
# Output: Hello\World!


