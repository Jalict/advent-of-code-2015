import md5, sys
key = "yzbqklnj"

num = 9
print "INT \tHASH"
for i in range(0, 100000000):
    m = md5.new(key + str(i)).hexdigest()
    try:
        if str(m[:6]) == "000000" and int(m[6:7]) < num:
            num = int(m[6:7])
            print str(i) + "\t" + str(m)
    except ValueError:
        continue
