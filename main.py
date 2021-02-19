import re
text = input("Enter Text:")
x = re.findall("(?:\s+|$)", text, flags=0) # find all spaces and end of line
print(len(x))
