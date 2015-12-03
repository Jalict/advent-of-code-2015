import StringIO
str = open('input.txt', 'r');
i = 0
k = 1

for char in str.read():
    if i == -1:
        break
    else:
        k += 1
    if char == '(':
        i += 1
    elif char == ')':
        i -= 1
print k
