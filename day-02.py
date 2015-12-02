import StringIO
str = open('day-02', 'r');

buffer = StringIO.StringIO(str.read())

squareFeetPaper = 0;
width = 0;
height = 0;
length = 0;

#for line in buffer:
line = buffer.next()

smallestEdge = 100;
firstIndex = line.find('x')
secondIndex = line.find('x', firstIndex+1)

length = int(line[0:firstIndex])
width = int(line[firstIndex+1:secondIndex])
height = int(line[secondIndex+1:])

if width < smallestEdge:
    smallestEdge = width
if height < smallestEdge:
    smallestEdge = height
if length < smallestEdge:
    smallestEdge = length

squareFeetPaper = squareFeetPaper + (2 * length * width) + (2 * width * height) + (2 * height * length) + smallestEdge
print line, ' = ', squareFeetPaper
print "29x13x26 = ", ((2 * 29 * 13) + (2 * 13 * 26) + (2 * 26 * 29) + 13)
