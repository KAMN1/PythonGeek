text = input() + " "
count = 0
unical = set()
for i in range(len(text)):
    if text[i] == " ":
        if " " not in (text[count: i]):
            unical.add(text[count:i])
            count = i+1
print(len(unical))