import StringIO
str = open('day-02', 'r');

buffer = StringIO.StringIO(str.read())

for line in buffer:
    print line

# Create int for square feet of wrapping paper
# Go through buffer, line
# substring the line into length, width and height
# find smallest edge
# square feet of wrapping paper += (2*l*w + 2*w*h + 2*h*l) + smallest edge
# Done!
