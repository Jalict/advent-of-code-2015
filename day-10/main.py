
NUM_OF_ITERATIONS = 40
currentNum = 1113122113
nextNum = ""

whichDigit = -1
howMany = 0

time = 0

for i in range(0,NUM_OF_ITERATIONS):
    print "Current Iteration: " + str(i)
    for digit in str(currentNum):
        if whichDigit != int(digit):
            if whichDigit != -1:
                nextNum += str(howMany) +""+ str(whichDigit)
            whichDigit = int(digit)
            howMany = 1
        else:
            howMany += 1
    nextNum += str(howMany) +""+ str(whichDigit)
    currentNum = int(nextNum)
print len(nextNum)

# This thing growths expontential, omg
