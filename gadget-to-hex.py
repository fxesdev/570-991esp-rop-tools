#!/usr/bin/python3
import sys
x = open(sys.argv[1])
c = 0
for line in x:
    c += 1
    e = line.strip()
    r = [i for i in e]
    cq = str(r[0])
    cw = str(r[2])
    ce = str(r[3])
    cr = str(r[4])
    ct = str(r[5])
    print(cr + ct + ' ' + cw + ce + ' x' + cq + ' xx ')
