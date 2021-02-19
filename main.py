n = 1
#
text = list((input("Enter Text:")).rstrip())
#
prev = object()
text = [prev:=v for v in text if prev!=v]
#
for i in list(text):
    if i == ' ':
        n += 1
print(n)
#
