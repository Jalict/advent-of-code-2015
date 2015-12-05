import StringIO
input = open('input.txt', 'r');

matrix = {}

str = input.readline()

xS = 0
yS = 0
xR = 0
yR = 0
houses = 1
isSanta = True
for c in str:
    try:
        if isSanta:
            matrix[xS,yS] += 1
        else:
            matrix[xR, yR] += 1
    except KeyError:
        if isSanta:
            matrix[xS,yS] = 1
        else:
            matrix[xR, yR] = 1
        houses += 1
    if c == "^":
        if isSanta:
            yS += 1
        else:
            yR += 1
    elif c == "v":
        if isSanta:
            yS -= 1
        else:
            yR -= 1
    elif c == "<":
        if isSanta:
            xS -= 1
        else:
            xR -= 1
    elif c == ">":
        if isSanta:
            xS += 1
        else:
            xR += 1
    else:
        print "Invalid Char"
    isSanta = not isSanta
print houses
