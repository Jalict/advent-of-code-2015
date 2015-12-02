import StringIO
str = open('day-02', 'r');

buffer = StringIO.StringIO(str.read())

for line in buffer:
    print line
