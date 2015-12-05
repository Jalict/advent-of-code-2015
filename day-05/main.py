import StringIO, re
txt = open('input.txt', 'r');

niceWordCount = 0
for word in txt:
    isNice = True

    reg = re.compile(r'([a-z])\1{1}') # Search for double [a-z]
    if reg.search(word) is None:
        isNice = False
    reg = re.compile(r'') # Search for three of those invidual [aeiou]
    if reg.search(word) is None:
        isNice = False
    reg = re.compile(r'') # does not contain ab, cd, pq or xy
    if reg.search(word) is None:
        isNice = False

    niceWordCount += 1 if isNice else 0
print niceWordCount
