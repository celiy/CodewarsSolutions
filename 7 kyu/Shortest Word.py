def find_short(s):
import re
s=s.replace("'","")
pattern = re.compile(r'\W+')

x = pattern.split(s)
return len(min(x, key=len))