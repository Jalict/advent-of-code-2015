import StringIO
str = open('day-02', 'r');

buffer = StringIO.StringIO(str.read())

squareFeetPaper = 0;
width = 0;
height = 0;
length = 0;

for line in buffer:
    # Format: 29x13x26
    # Values: length * width * height
    firstIndex = line.find('x')
    secondIndex = line.find('x', firstIndex+1)

    length = int(line[0:firstIndex])
    width  = int(line[firstIndex+1:secondIndex])
    height = int(line[secondIndex+1:])

    edges = [length, width, height]
    edges.sort()

    # Calculate: 2*l*w + 2*w*h + 2*h*l
    squareFeetPaper = squareFeetPaper + (2 * length * width) + (2 * width * height) + (2 * height * length) + (edges[0] * edges[1])
    print line, ' = ', ((2 * length * width) + (2 * width * height) + (2 * height * length) + (edges[0] * edges[1]))
print squareFeetPaper
