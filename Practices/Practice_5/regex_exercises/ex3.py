import re 

strings = ["a_c","hello_world","Hello_World","h0me_dome","a__c"]

for s in strings:
    if re.fullmatch(r"[a-z]+_[a-z]+", s):
        print(f"Matched: {s}")
print()

str = "This is my lap_top a_nd B_ag, ph_0ne"
d = re.findall(r"[a-z]+_[a-z]+",str)
print(f"Matched: {d}" )
