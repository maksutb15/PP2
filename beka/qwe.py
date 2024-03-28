path = "text.txt"
save = ""
with open(path, "r") as f:
    save = f.read()
    
import re 

res = re.sub('.{1}',  lambda x: str(ord(x.group())), save)

with open(path, "w") as f:
    f.write(res)