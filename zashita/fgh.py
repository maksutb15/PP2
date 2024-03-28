path = "C:/Users/maksu/Documents/pythonwww/zashita/text.txt"
save = ""
with open(path, "r") as f:
    save = f.read()
with open(path, "w") as f:
    for i in save:
        if i.isalpha():
            f.write(str(ord(i)))
        else:
            f.write(i)