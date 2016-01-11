#!/usr/local/bin/python
import md5

seed = "yzbqklnj"
i = 0
while True:
  test = seed + str(i)
  testHash = md5.new(test)
  if (testHash.hexdigest().startswith("000000")):
    print "Found answer: %i" % i
    break
  i += 1
